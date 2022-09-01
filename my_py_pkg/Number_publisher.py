#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64

class Number_publisher(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("Num_pub") # MODIFY NAME

        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(1, self.send_num)
        self.get_logger().info("Num_Pub has been started")

    def send_num(self):
        msg = Int64()
        msg.data = 1
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Number_publisher() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
