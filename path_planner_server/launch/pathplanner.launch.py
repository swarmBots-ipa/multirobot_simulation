import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    controller_yaml_barista_0 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_0_controller.yaml')
    bt_navigator_yaml_barista_0 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_0_bt_navigator.yaml')
    planner_yaml_barista_0 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_0_planner_server.yaml')
    recovery_yaml_barista_0 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_0_recovery.yaml')

    controller_yaml_barista_1 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_1_controller.yaml')
    bt_navigator_yaml_barista_1 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_1_bt_navigator.yaml')
    planner_yaml_barista_1 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_1_planner_server.yaml')
    recovery_yaml_barista_1 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_1_recovery.yaml')

    controller_yaml_barista_2 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_2_controller.yaml')
    bt_navigator_yaml_barista_2 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_2_bt_navigator.yaml')
    planner_yaml_barista_2 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_2_planner_server.yaml')
    recovery_yaml_barista_2 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_2_recovery.yaml')

    controller_yaml_barista_3 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_3_controller.yaml')
    bt_navigator_yaml_barista_3 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_3_bt_navigator.yaml')
    planner_yaml_barista_3 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_3_planner_server.yaml')
    recovery_yaml_barista_3 = os.path.join(get_package_share_directory(
        'path_planner_server'), 'config', 'barista_3_recovery.yaml')

    return LaunchDescription([

        # Nodes for barista_0

        Node(
            namespace='barista_0',
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[controller_yaml_barista_0]),

        Node(
            namespace='barista_0',
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[planner_yaml_barista_0]),

        Node(
            namespace='barista_0',
            package='nav2_recoveries',
            executable='recoveries_server',
            name='recoveries_server',
            parameters=[recovery_yaml_barista_0],
            output='screen'),

        Node(
            namespace='barista_0',
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[bt_navigator_yaml_barista_0]),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='barista_0_lifecycle_manager_pathplanner',
            output='screen',
            parameters=[{'autostart': True},
                        {'bond_timeout': 0.0},
                        {'node_names': [
                            'barista_0/planner_server',
                            'barista_0/controller_server',
                            'barista_0/recoveries_server',
                            'barista_0/bt_navigator'
                        ]}]),



        # Nodes for barista_1

        Node(
            namespace='barista_1',
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[controller_yaml_barista_1]),

        Node(
            namespace='barista_1',
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[planner_yaml_barista_1]),

        Node(
            namespace='barista_1',
            package='nav2_recoveries',
            executable='recoveries_server',
            name='recoveries_server',
            parameters=[recovery_yaml_barista_1],
            output='screen'),

        Node(
            namespace='barista_1',
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[bt_navigator_yaml_barista_1]),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='barista_1_lifecycle_manager_pathplanner',
            output='screen',
            parameters=[{'autostart': True},
                        {'bond_timeout': 0.0},
                        {'node_names': [
                            'barista_1/planner_server',
                            'barista_1/controller_server',
                            'barista_1/recoveries_server',
                            'barista_1/bt_navigator'
                        ]}]),

        # Nodes for barista_2

        Node(
            namespace='barista_2',
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[controller_yaml_barista_2]),

        Node(
            namespace='barista_2',
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[planner_yaml_barista_2]),

        Node(
            namespace='barista_2',
            package='nav2_recoveries',
            executable='recoveries_server',
            name='recoveries_server',
            parameters=[recovery_yaml_barista_2],
            output='screen'),

        Node(
            namespace='barista_2',
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[bt_navigator_yaml_barista_2]),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='barista_2_lifecycle_manager_pathplanner',
            output='screen',
            parameters=[{'autostart': True},
                        {'bond_timeout': 0.0},
                        {'node_names': [
                            'barista_2/planner_server',
                            'barista_2/controller_server',
                            'barista_2/recoveries_server',
                            'barista_2/bt_navigator'
                        ]}]),

        # Nodes for barista_3

        Node(
            namespace='barista_3',
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[controller_yaml_barista_3]),

        Node(
            namespace='barista_3',
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[planner_yaml_barista_3]),

        Node(
            namespace='barista_3',
            package='nav2_recoveries',
            executable='recoveries_server',
            name='recoveries_server',
            parameters=[recovery_yaml_barista_3],
            output='screen'),

        Node(
            namespace='barista_3',
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[bt_navigator_yaml_barista_3]),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='barista_3_lifecycle_manager_pathplanner',
            output='screen',
            parameters=[{'autostart': True},
                        {'bond_timeout': 0.0},
                        {'node_names': [
                            'barista_3/planner_server',
                            'barista_3/controller_server',
                            'barista_3/recoveries_server',
                            'barista_3/bt_navigator'
                        ]}])
    ])
