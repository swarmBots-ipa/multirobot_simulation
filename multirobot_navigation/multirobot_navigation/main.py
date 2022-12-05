#! /usr/bin/env python3

import rclpy
from rclpy.executors import SingleThreadedExecutor
from multirobot_navigation.robot_goal_publisher import GoalPublisher
from multirobot_navigation.compute_pallet_poses import ComputeEdgePose


def main(args=None):
    """Start the pallet edge pose estimation 
    send the pose to each robot in the swarm

    The swarm can be scaled up and down by 
    modifying the ComputeEdgePose to generate 
    more points in pallet vertices.
    """
    rclpy.init(args=args)
    try:
        pallet_pose_publisher = ComputeEdgePose(width=1.6, height=1)
        action_client_robot_0 = GoalPublisher(robot_id=0)
        action_client_robot_1 = GoalPublisher(robot_id=1)
        action_client_robot_2 = GoalPublisher(robot_id=2)
        action_client_robot_3 = GoalPublisher(robot_id=3)
        executor = SingleThreadedExecutor()

        executor.add_node(pallet_pose_publisher)
        executor.add_node(action_client_robot_0)
        executor.add_node(action_client_robot_1)
        executor.add_node(action_client_robot_2)
        executor.add_node(action_client_robot_3)

        try:
            executor.spin()
        finally:
            executor.shutdown()
            pallet_pose_publisher.destroy_node()

    except KeyboardInterrupt:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
