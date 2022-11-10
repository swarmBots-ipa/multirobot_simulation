import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    barista_0_config = os.path.join(get_package_share_directory(
        'localization_server'), 'config', 'barista_0_amcl_config.yaml')
    barista_1_config = os.path.join(get_package_share_directory(
        'localization_server'), 'config', 'barista_1_amcl_config.yaml')
    barista_2_config = os.path.join(get_package_share_directory(
        'localization_server'), 'config', 'barista_2_amcl_config.yaml')
    barista_3_config = os.path.join(get_package_share_directory(
        'localization_server'), 'config', 'barista_3_amcl_config.yaml')

    map_file = os.path.join(get_package_share_directory(
        'localization_server'), 'config', 'empty_room.yaml')

    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'topic_name': "map"},
                        {'frame_id': "map"},
                        {'yaml_filename': map_file}]
        ),

        Node(
            namespace='barista_0',
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[barista_0_config]
        ),

        Node(
            namespace='barista_1',
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[barista_1_config]
        ),

        Node(
            namespace='barista_2',
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[barista_2_config]
        ),

        Node(
            namespace='barista_3',
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[barista_3_config]
        ),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'autostart': True},
                        {'bond_timeout': 0.0},
                        {'node_names': ['map_server', 'barista_0/amcl', 'barista_1/amcl', 'barista_2/amcl', 'barista_3/amcl']}]
        )
    ])
