from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    number_publisher_node = Node(
        package="my_py_pkg",
        executable="Number_pub",
        name="my_num_pub",
        remappings=[("number", "my_number")
        ],
        parameters=[
            {"number_to_pub": 4}
        ]
    )

    counter_node = Node(
        package="my_py_pkg",
        executable="counter_",
        name="my_num_count",
        remappings=[("number", "my_number"),("number_count", "my_number_count")
        ]
    )


    ld.add_action(number_publisher_node)
    ld.add_action(counter_node)
    return ld