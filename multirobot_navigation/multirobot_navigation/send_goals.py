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
        navigator=BasicNavigator()
        current_pose = PoseStamped()
        current_pose.header.frame_id = 'map'
        current_pose.header.stamp = Node.get_clock(self).now().to_msg()
        current_pose.pose.position.x = 1.0
        current_pose.pose.position.y = 1.0
        current_pose.pose.position.z = 0.0
        current_pose.pose.orientation.x = 0.0
        current_pose.pose.orientation.y = 0.0
        current_pose.pose.orientation.z = 0.7071067811865476
        current_pose.pose.orientation.w = 0.7071067811865476
        self.get_logger().info('Sending goal Pose B')
        self.publish_goal_B.publish(current_pose)
        navigator.setInitialPose(current_pose)

        navigator.waitUntilNav2Active()

        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock(self).now().to_msg()
        goal_pose.pose.position.x = 1.0
        goal_pose.pose.position.y = 1.0
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.7071067811865476
        goal_pose.pose.orientation.w = 0.7071067811865476
        navigator.goToPose(goal_pose)

        path = navigator.getPath(init_pose, goal_pose)
        smoothed_path = navigator.smoothPath(path)
        print(smoothed_path)
        # i = 0
        # while not navigator.isTaskComplete():
        #     ################################################
        #     #
        #     # Implement some code here for your application!
        #     #
        #     ################################################

        #     # Do something with the feedback
        #     i = i + 1
        #     feedback = navigator.getFeedback()
        #     if feedback and i % 5 == 0:
        #         print('Estimated time of arrival: ' + '{0:.0f}'.format(
        #             Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
        #             + ' seconds.')

        #         # Some navigation timeout to demo cancellation
        #         if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
        #             navigator.cancelTask()

        #         # Some navigation request change to demo preemption
        #         if Duration.from_msg(feedback.navigation_time) > Duration(seconds=18.0):
        #             goal_pose.pose.position.x = -3.0
        #             navigator.goToPose(goal_pose)

        # # Do something depending on the return code
        # result = navigator.getResult()
        # if result == TaskResult.SUCCEEDED:
        #     print('Goal succeeded!')
        # elif result == TaskResult.CANCELED:
        #     print('Goal was canceled!')
        # elif result == TaskResult.FAILED:
        #     print('Goal failed!')
        # else:
        #     print('Goal has an invalid return status!')

        # navigator.lifecycleShutdown()


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
