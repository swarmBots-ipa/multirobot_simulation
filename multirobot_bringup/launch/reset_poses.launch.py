from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    node = Node(
        package='multirobot_navigation',
        name='reset_poses',
        executable='reset_robot_pose'
    )
    ld.add_action(node)
    return ld
