from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node


class NavToPoseActionClient(Node):

    def __init__(self):
        super().__init__('move_to_spot',
                         allow_undeclared_parameters=True,
                         automatically_declare_parameters_from_overrides=True)

        self._action_client = ActionClient(self, NavigateToPose, 'NavigateToPose')

    def send_goal(self):

        recived_spot_name = (self.get_parameter_or('spot_name'))
        param = str(recived_spot_name.value)
        
        print(param+'.x')

        posex = (self.get_parameter_or(param+'.x'))
        posey = (self.get_parameter_or(param+'.y'))
        posez = (self.get_parameter_or(param+'.z'))

        poseox = (self.get_parameter_or(param+'.ox'))
        poseoy = (self.get_parameter_or(param+'.oy'))
        poseoz = (self.get_parameter_or(param+'.oz'))
        poseow = (self.get_parameter_or(param+'.ow'))

        goal_pose = NavigateToPose.Goal()
        goal_pose.pose.header.frame_id = 'map'
        goal_pose.pose.pose.position.x = posex.value
        goal_pose.pose.pose.position.y = posey.value
        goal_pose.pose.pose.position.z = posez.value
        goal_pose.pose.pose.orientation.x = poseox.value
        goal_pose.pose.pose.orientation.y = poseoy.value
        goal_pose.pose.pose.orientation.z = poseoz.value
        goal_pose.pose.pose.orientation.w = poseow.value

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(
            goal_pose,
            feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
            
        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()

        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):

        result = future.result().result
        status = future.result().status
        
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Navigation succeeded! ')
        else:
            self.get_logger().info('Navigation failed with status: {0}'.format(status))

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback

def main(args=None):
    rclpy.init(args=args)

    action_client = NavToPoseActionClient()

    action_client.send_goal()

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()