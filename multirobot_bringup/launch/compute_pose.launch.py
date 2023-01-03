import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    node = Node(
        package='multirobot_navigation',
        name='computed_edge_poses',
        executable='compute_pallet_pose',
    )
    ld.add_action(node)
    return ld
