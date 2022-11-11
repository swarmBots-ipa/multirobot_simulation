from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "package_name",
            default_value="localization_server",
        )
    )
    package_name = LaunchConfiguration("package_name")

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare(package_name), "config", "rviz_config.rviz"]
    )


    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    nodes_to_start = [
        rviz_node
    ]

    return LaunchDescription(declared_arguments + nodes_to_start)