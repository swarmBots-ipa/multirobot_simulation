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
        super().__init__('goal_publisher')
        # Create publishers
        self.publish_goal_A = self.create_publisher(
            PoseStamped, 'barista_0/goal_pose', 10)
        self.publish_goal_B = self.create_publisher(
            PoseStamped, 'barista_1/goal_pose', 10)
        self.publish_goal_C = self.create_publisher(
            PoseStamped, 'barista_2/goal_pose', 10)
        self.publish_goal_D = self.create_publisher(
            PoseStamped, 'barista_3/goal_pose', 10)

        self.set_pose_A()
        self.set_pose_B()
        self.set_pose_C()
        self.set_pose_D()

    def set_pose_A(self):
        """
        Callback function.
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = 2.0
        goal_pose.pose.position.y = 3.0
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose A')
        self.publish_goal_A.publish(goal_pose)

    def set_pose_B(self):
        """
        Callback function.
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = 2.0
        goal_pose.pose.position.y = 2.0
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose B')
        self.publish_goal_B.publish(goal_pose)

    def set_pose_C(self):
        """
        Callback function.
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = 3.0
        goal_pose.pose.position.y = 2.0
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose C')
        self.publish_goal_C.publish(goal_pose)

    def set_pose_D(self):
        """
        Callback function.
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = 3.0
        goal_pose.pose.position.y = 3.0
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose D')
        self.publish_goal_D.publish(goal_pose)


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
