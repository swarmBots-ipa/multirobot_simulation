#! /usr/bin/env python3

from geometry_msgs.msg import PoseStamped
import rclpy
from rclpy.node import Node

from math import sin
from math import cos
from math import degrees
from math import atan2


class ComputeEdgePose(Node):

    def __init__(self):
        """
        Class constructor to set up the node
        """
        # Initiate the Node class's constructor and give it a name
        super().__init__('pallet_pose_publisher')
        # Create publishers to send goals to each robot
        self.publish_edge_A = self.create_publisher(
            PoseStamped, 'barista_0/goal_pose', 10)
        self.publish_edge_B = self.create_publisher(
            PoseStamped, 'barista_1/goal_pose', 10)
        self.publish_edge_C = self.create_publisher(
            PoseStamped, 'barista_2/goal_pose', 10)
        self.publish_edge_D = self.create_publisher(
            PoseStamped, 'barista_3/goal_pose', 10)
        self.subscribe_palette_center = self.create_subscription(
            PoseStamped, 'palette/goal_pose', self.get_palette_center_cb, 10)

    def get_palette_center_cb(self, pose):
        """
        Callback Function to triger the compute_edge_pose() 
        """
        # convert the quaternion to theta
        t3 = +2.0 * (pose.pose.orientation.w * pose.pose.orientation.z +
                     pose.pose.orientation.x * pose.pose.orientation.y)
        t4 = +1.0 - 2.0 * (pose.pose.orientation.y * pose.pose.orientation.y +
                           pose.pose.orientation.z * pose.pose.orientation.z)
        yaw = atan2(t3, t4)
        # send the center coordinates of the palett to estimate its edges
        self.compute_edge_pose(center_x=pose.pose.position.x,
                               center_y=pose.pose.position.y,
                               center_theta=yaw,
                               length=1.4,
                               height=0.8)

    def compute_edge_pose(self, center_x, center_y, center_theta, length, height):
        """
        Function to estimate the edge poses of the palette
        """
        self.center_x = center_x  # geometric center x of the palette
        self.center_y = center_y  # geometric center y of the palette
        # orientation of the palette wrt the map
        self.theta = degrees(center_theta)
        self.length = length  # longest side of the palette
        self.height = height  # shortest side of the palette

        aX, aY = self.center_x - 0.5*self.length*(sin(self.theta) + cos(
            self.theta)), self.center_y - 0.5*self.height*(sin(self.theta) - cos(self.theta))
        bX, bY = self.center_x + 0.5*self.length*(sin(self.theta) - cos(
            self.theta)), self.center_y - 0.5*self.height*(sin(self.theta) + cos(self.theta))
        cX, cY = self.center_x + 0.5*self.length*(sin(self.theta) + cos(
            self.theta)), self.center_y + 0.5*self.height*(sin(self.theta) - cos(self.theta))
        dX, dY = self.center_x - 0.5*self.length*(sin(self.theta) - cos(
            self.theta)), self.center_y + 0.5*self.height*(sin(self.theta) + cos(self.theta))

        self.set_pose_A(aX, aY)
        self.set_pose_B(bX, bY)
        self.set_pose_C(cX, cY)
        self.set_pose_D(dX, dY)

    def set_pose_A(self, aX, aY):
        """
        Callback function.
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = float(aX)
        goal_pose.pose.position.y = float(aY)
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose A')
        self.publish_edge_A.publish(goal_pose)

    def set_pose_B(self, bX, bY):
        """
        Callback function.
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = float(bX)
        goal_pose.pose.position.y = float(bY)
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose B')
        self.publish_edge_B.publish(goal_pose)

    def set_pose_C(self, cX, cY):
        """
        Callback function.
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = float(cX)
        goal_pose.pose.position.y = float(cY)
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose C')
        self.publish_edge_C.publish(goal_pose)

    def set_pose_D(self, dX, dY):
        """
        Callback function.
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = float(dX)
        goal_pose.pose.position.y = float(dY)
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose D')
        self.publish_edge_D.publish(goal_pose)


def main(args=None):

    rclpy.init(args=args)
    try:
        pallet_pose_publisher = ComputeEdgePose()
        rclpy.spin(pallet_pose_publisher)
    except KeyboardInterrupt:
        pallet_pose_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
