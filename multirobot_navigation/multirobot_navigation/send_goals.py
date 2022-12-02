#! /usr/bin/env python3

from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node


class GoalPublisher(Node):

    def __init__(self):
        super().__init__('goal_publisher',
                         allow_undeclared_parameters=True,
                         automatically_declare_parameters_from_overrides=True)

        self._action_client_0 = ActionClient(
            self, NavigateToPose, '/barista_0/navigate_to_pose')

    def send_goal(self):
        goal_pose = NavigateToPose.Goal()
        goal_pose.pose.header.frame_id = 'map'
        goal_pose.pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.pose.position.x = 2.0
        goal_pose.pose.pose.position.y = 3.0
        goal_pose.pose.pose.position.z = 0.0
        goal_pose.pose.pose.orientation.x = 0.0
        goal_pose.pose.pose.orientation.y = 0.0
        goal_pose.pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.pose.orientation.w = 0.7071067811865476

        self._action_client_0.wait_for_server()

        self._send_goal_future = self._action_client_0.send_goal_async(
            goal_pose,
            feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Navigation succeeded! ')
        else:
            self.get_logger().info(
                'Navigation failed with status: {0}'.format(status))

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback


def main(args=None):
    rclpy.init(args=args)
    try:
        action_client = GoalPublisher()
        action_client.send_goal()
        rclpy.spin(action_client)
    except KeyboardInterrupt:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
