#! /usr/bin/env python3

from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus
from geometry_msgs.msg import PoseStamped

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node


class GoalPublisher(Node):

    def __init__(self, robot_id):
        super().__init__(str('goal_publisher_client_'+str(robot_id)),
                         allow_undeclared_parameters=True,
                         automatically_declare_parameters_from_overrides=True)
        # subscribes the pallet edge poses
        subscription_topic  = 'barista_'+str(robot_id)+'/send_pose'
        action_topic = '/barista_'+str(robot_id)+'/navigate_to_pose'
        self.ROBOT_ID = robot_id
        self.subscribe_pose = self.create_subscription(
            PoseStamped, subscription_topic, self.send_pose, 10)
        self.nav_to_pose_action_client = ActionClient(
            self, NavigateToPose, action_topic)


    def send_pose(self, pose):
        goal_pose = NavigateToPose.Goal()
        goal_pose.pose.header.frame_id = pose.header.frame_id
        goal_pose.pose.header.stamp = pose.header.stamp
        goal_pose.pose.pose.position.x = pose.pose.position.x
        goal_pose.pose.pose.position.y = pose.pose.position.y
        goal_pose.pose.pose.position.z = pose.pose.position.z
        goal_pose.pose.pose.orientation.x = pose.pose.orientation.x
        goal_pose.pose.pose.orientation.y = pose.pose.orientation.y
        goal_pose.pose.pose.orientation.z = pose.pose.orientation.z
        goal_pose.pose.pose.orientation.w = pose.pose.orientation.w

        self.nav_to_pose_action_client.wait_for_server()
        self._send_goal_future = self.nav_to_pose_action_client.send_goal_async(
            goal_pose,
            feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected by {0}'.format(self.ROBOT_ID))
            return
        self.get_logger().info('Goal accepted by {0}'.format(self.ROBOT_ID))
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        # PENDING=0
        # ACTIVE=1
        # PREEMPTED=2
        # SUCCEEDED=3
        # ABORTED=4
        # REJECTED=5
        # PREEMPTING=6
        # RECALLING=7
        # RECALLED=8
        # LOST=9
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Navigation succeeded for Robot_{0}'.format(self.ROBOT_ID))
        else:
            self.get_logger().info(
                'Navigation failed for Robot_{0} with status: {0}'.format(self.ROBOT_ID,status))

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback


def main(args=None):
    rclpy.init(args=args)
    try:
        action_client_robot_0 = GoalPublisher(robot_id=2)
        rclpy.spin(action_client_robot_0)
    except KeyboardInterrupt:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
