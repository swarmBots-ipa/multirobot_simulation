#! /usr/bin/env python3

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration


class GoalPublisher(Node):

    def __init__(self):
        """
        Class constructor to set up the node
        """
        # Initiate the Node class's constructor and give it a name
        super().__init__('initial_pose_publisher')
        # Create publishers
        self.publish_goal_A = self.create_publisher(
            PoseStamped, 'barista_0/goal_pose', 10)
        self.publish_goal_B = self.create_publisher(
            PoseStamped, 'barista_1/goal_pose', 10)
        self.publish_goal_C = self.create_publisher(
            PoseStamped, 'barista_2/goal_pose', 10)
        self.publish_goal_D = self.create_publisher(
            PoseStamped, 'barista_3/goal_pose', 10)

        self.reset_pose_A()
        self.reset_pose_B()
        self.reset_pose_C()
        self.reset_pose_D()

    def reset_pose_A(self):
        """
        Callback function.
        """
        initialpose = PoseStamped()
        initialpose.header.frame_id = 'map'
        initialpose.header.stamp = Node.get_clock(self).now().to_msg()
        initialpose.pose.position.x = 1.0
        initialpose.pose.position.y = 1.0
        initialpose.pose.position.z = 0.0
        initialpose.pose.orientation.x = 0.0
        initialpose.pose.orientation.y = 0.0
        initialpose.pose.orientation.z = 0.7071067811865476
        initialpose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose A')
        self.publish_goal_A.publish(initialpose)

    def reset_pose_B(self):
        """
        Callback function.
        """
        initialpose = PoseStamped()
        initialpose.header.frame_id = 'map'
        initialpose.header.stamp = Node.get_clock(self).now().to_msg()
        initialpose.pose.position.x = 2.0
        initialpose.pose.position.y = 1.0
        initialpose.pose.position.z = 0.0
        initialpose.pose.orientation.x = 0.0
        initialpose.pose.orientation.y = 0.0
        initialpose.pose.orientation.z = 0.7071067811865476
        initialpose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose B')
        self.publish_goal_B.publish(initialpose)

    def reset_pose_C(self):
        """
        Callback function.
        """
        initialpose = PoseStamped()
        initialpose.header.frame_id = 'map'
        initialpose.header.stamp = Node.get_clock(self).now().to_msg()
        initialpose.pose.position.x = 3.0
        initialpose.pose.position.y = 1.0
        initialpose.pose.position.z = 0.0
        initialpose.pose.orientation.x = 0.0
        initialpose.pose.orientation.y = 0.0
        initialpose.pose.orientation.z = 0.7071067811865476
        initialpose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose C')
        self.publish_goal_C.publish(initialpose)

    def reset_pose_D(self):
        """
        Callback function.
        """
        initialpose = PoseStamped()
        initialpose.header.frame_id = 'map'
        initialpose.header.stamp = Node.get_clock(self).now().to_msg()
        initialpose.pose.position.x = 4.0
        initialpose.pose.position.y = 1.0
        initialpose.pose.position.z = 0.0
        initialpose.pose.orientation.x = 0.0
        initialpose.pose.orientation.y = 0.0
        initialpose.pose.orientation.z = 0.7071067811865476
        initialpose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose D')
        self.publish_goal_D.publish(initialpose)


def main(args=None):

    rclpy.init(args=args)
    try:
        goal_publisher = GoalPublisher()
        rclpy.spin(goal_publisher)
    except KeyboardInterrupt:
        goal_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
