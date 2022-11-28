#! /usr/bin/env python3

from geometry_msgs.msg import PoseStamped
import rclpy
from rclpy.node import Node

from math import sin
from math import cos
from math import degrees, radians
from math import atan2

class ComputeEdgePose(Node):
    """Compute the edge poses of the palette and publish the poses to the robots.
    """
    def __init__(self):

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
        """A callback to subscribe to 'palette/goal_pose'
            and trigger compute_edge_pose()

        Args:
            pose (PoseStamped): pose of the geometric center of the palette 
        """
        self.compute_edge_pose(pose,
                               width=1.5,
                               height=1)

    def compute_edge_pose(self, pose, width, height):
        """Compute the poses of robots 0-3 and send them to the robots

        Args:
            center_x (float): geometric center x 
            center_y (float): geometric center y 
            orientation_z (_type_): geometric center
            orientation_w (_type_): geometric center
            width (int): longest side of the palette
            height (int): shortest side of the palette
        """
        # convert the quaternion to angle
        t3 = +2.0 * (pose.pose.orientation.w * pose.pose.orientation.z +
                     pose.pose.orientation.x * pose.pose.orientation.y)
        t4 = +1.0 - 2.0 * (pose.pose.orientation.y * pose.pose.orientation.y +
                           pose.pose.orientation.z * pose.pose.orientation.z)
        yaw = atan2(t3, t4)
        
        self.center_x = pose.pose.position.x  # geometric center x of the palette
        self.center_y = pose.pose.position.y  # geometric center y of the palette
        # orientation of the palette wrt the map
        self.orientation_z=pose.pose.orientation.z
        self.orientation_w=pose.pose.orientation.w
        self.angle = radians(yaw) # angle should be in radians
        self.width = width  # longest side of the palette
        self.height = height  # shortest side of the palette

        aX, aY = self.center_x - 0.5*self.width*(sin(self.angle) + cos(
            self.angle)), self.center_y - 0.5*self.height*(sin(self.angle) - cos(self.angle))
        bX, bY = self.center_x + 0.5*self.width*(sin(self.angle) - cos(
            self.angle)), self.center_y - 0.5*self.height*(sin(self.angle) + cos(self.angle))
        cX, cY = self.center_x + 0.5*self.width*(sin(self.angle) + cos(
            self.angle)), self.center_y + 0.5*self.height*(sin(self.angle) - cos(self.angle))
        dX, dY = self.center_x - 0.5*self.width*(sin(self.angle) - cos(
            self.angle)), self.center_y + 0.5*self.height*(sin(self.angle) + cos(self.angle))

        self.set_pose_A(aX, aY, self.orientation_z, self.orientation_w)
        self.set_pose_B(bX, bY, self.orientation_z, self.orientation_w)
        self.set_pose_C(cX, cY, self.orientation_z, self.orientation_w)
        self.set_pose_D(dX, dY, self.orientation_z, self.orientation_w)

    def set_pose_A(self, aX, aY, orientation_z, orientation_w,):
        """publish pose to Robot A

        Args:
            aX (float): x
            aY (float): y
            orientation_z (float): quaternions z
            orientation_w (float): quaternions w
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = float(aX)
        goal_pose.pose.position.y = float(aY)
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = orientation_z
        goal_pose.pose.orientation.w = orientation_w
        self.get_logger().info('Sending goal to robot A')
        self.publish_edge_A.publish(goal_pose)

    def set_pose_B(self, bX, bY, orientation_z, orientation_w,):
        """publish pose to Robot B

        Args:
            bX (float): x
            bY (float): y
            orientation_z (float): quaternions z
            orientation_w (float): quaternions w
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = float(bX)
        goal_pose.pose.position.y = float(bY)
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = orientation_z
        goal_pose.pose.orientation.w = orientation_w
        self.get_logger().info('Sending goal to robot B')
        self.publish_edge_B.publish(goal_pose)

    def set_pose_C(self, cX, cY, orientation_z, orientation_w,):
        """publish pose to Robot C

        Args:
            cX (float): x
            cY (float): y
            orientation_z (float): quaternions z
            orientation_w (float): quaternions w
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = float(cX)
        goal_pose.pose.position.y = float(cY)
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = orientation_z
        goal_pose.pose.orientation.w = orientation_w
        self.get_logger().info('Sending goal to robot C')
        self.publish_edge_C.publish(goal_pose)

    def set_pose_D(self, dX, dY, orientation_z, orientation_w,):
        """publish pose to Robot D

        Args:
            dX (float): x
            dY (float): y
            orientation_z (float): quaternions z
            orientation_w (float): quaternions w
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = float(dX)
        goal_pose.pose.position.y = float(dY)
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = orientation_z
        goal_pose.pose.orientation.w = orientation_w
        self.get_logger().info('Sending goal to robot D')
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