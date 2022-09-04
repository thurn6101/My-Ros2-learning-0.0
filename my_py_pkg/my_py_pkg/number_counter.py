#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool


class Number_counter(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("Counter_")  # MODIFY NAME
        self.n = 0
        self.server_ = self.create_service(
            SetBool, "reset_counter", self.callback_reset_counter)
        self.subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number, 10)
        self.get_logger().info("counter_sub has been started")

        # This publisher no need for timer because it depend on the timer on the previous publisher node
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)

    def callback_reset_counter(self, request, response):
        if request.data:
            self.n = 0
            response.success = True
            response.message = "Counter has been reset"
        else:
            response.success = False
            response.message = "Counter has not been reset"
        return response

    def callback_number(self, msg):
        self.n += msg.data  # input the last data from the last publisher node into n
        msg1 = Int64()  # the last 3 line use for this node publisher
        msg1.data = self.n
        self.publisher_.publish(msg1)


def main(args=None):
    rclpy.init(args=args)
    node = Number_counter()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
