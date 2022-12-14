import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    #config = os.path.join(get_package_share_directory(
    #    'multirobot_bringup'), 'config', 'pose-list.yaml')

    node = Node(
        package='multirobot_navigation',
        name='send_pallet_pose',
        executable='send_pallet_pose',
        #parameters=[config]
    )
    ld.add_action(node)
    return ld
