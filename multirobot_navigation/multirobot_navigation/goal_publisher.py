#! /usr/bin/env python3

from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus
from geometry_msgs.msg import PoseStamped

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node


class GoalPublisher(Node):

    def __init__(self):
        super().__init__('goal_publisher',
                         allow_undeclared_parameters=True,
                         automatically_declare_parameters_from_overrides=True)
        # subscribes the pallet edge poses
        self.subscribe_pose_0 = self.create_subscription(
            PoseStamped, 'barista_0/send_pose', self.get_pose_A, 10)
        # self.subscribe_pose_1 = self.create_subscription(
        #     PoseStamped, 'barista_1/send_pose', self.get_pose_B, 10)
        # self.subscribe_pose_2 = self.create_subscription(
        #     PoseStamped, 'barista_2/send_pose', self.get_pose_C, 10)
        # self.subscribe_pose_3 = self.create_subscription(
        #     PoseStamped, 'barista_3/send_pose', self.get_pose_D, 10)

        self._action_client_0 = ActionClient(
            self, NavigateToPose, '/barista_0/navigate_to_pose')
        # self._action_client_1 = ActionClient(
        #     self, NavigateToPose, '/barista_1/navigate_to_pose')

    def get_pose_A(self, pose):
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

        self._action_client_0.wait_for_server()
        self._send_goal_future = self._action_client_0.send_goal_async(
            goal_pose,
            feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_A_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected by Robot_0')
            return
        self.get_logger().info('Goal accepted by Robot_0')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_A_callback(self, future):
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
            self.get_logger().info('Navigation succeeded for Robot_0!')
        else:
            self.get_logger().info(
                'Navigation failed for Robot_0 with status: {0}'.format(status))

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback


def main(args=None):
    rclpy.init(args=args)
    try:
        action_client_nav2 = GoalPublisher()
        rclpy.spin(action_client_nav2)
    except KeyboardInterrupt:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
