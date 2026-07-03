from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Define launch arguments
    safety_zone_arg = DeclareLaunchArgument('safety_zone', default_value='2.0')
    robot_priority_arg = DeclareLaunchArgument('robot_priority', default_value='3')
    robot_position_x_arg = DeclareLaunchArgument('robot_position_x', default_value='30.0')
    robot_position_y_arg = DeclareLaunchArgument('robot_position_y', default_value='30.0')

    # Fleet simulator node
    fleet_node = Node(
        package='traffic_system',
        executable='fleet_simulator',
        name='fleet_simulator'
    )

    # Traffic manager node with parameters
    traffic_node = Node(
        package='traffic_system',
        executable='traffic_manager',
        name='traffic_manager',
        parameters=[{
            'safety_zone': LaunchConfiguration('safety_zone'),
            'robot_priority': LaunchConfiguration('robot_priority'),
            'robot_position_x': LaunchConfiguration('robot_position_x'),
            'robot_position_y': LaunchConfiguration('robot_position_y')
        }]
    )

    return LaunchDescription([
        safety_zone_arg,
        robot_priority_arg,
        robot_position_x_arg,
        robot_position_y_arg,
        fleet_node,
        traffic_node
    ])