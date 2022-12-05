import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    node = Node(
        package='multirobot_navigation',
        name='send_edge_poses',
        executable='main_function',
    )
    ld.add_action(node)
    return ld
