#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

from my_robot_interfaces.srv import BatteryState


class Battery(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("Battery")  # MODIFY NAME
        self.battery_state_ = "full"
        self.last_time_battery_state_changed_ = self.get_current_time_seconds()
        self.battery_timer_ = self.create_timer(0.1, self.check_battery_state)
        self.get_logger().info("Battery node has been started")

    def get_current_time_seconds(self):
        secs, nsecs = self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs / 1000000000.0

    def check_battery_state(self):
        time_now = self.get_current_time_seconds()
        if self.battery_state_ == "full":
            if time_now - self.last_time_battery_state_changed_ > 4.0:
                self.battery_state_ = "empty"
                self.get_logger().info("Battery is empty! Charging battery...")
                self.last_time_battery_state_changed_ = time_now
                self.call_set_led_server(3, 1)

        else:
            if time_now - self.last_time_battery_state_changed_ > 6.0:
                self.battery_state_ = "full"
                self.get_logger().info("Battery is full!")
                self.last_time_battery_state_changed_ = time_now
                self.call_set_led_server(3, 0)

    def call_set_led_server(self, led_number, state):
        client = self.create_client(BatteryState, "set_led")
        while not client.wait_for_service(1.0):
            node.get_logger().warn("Waiting for Server set led...")

        request = BatteryState.Request()
        request.led_number = led_number
        request.state = state


        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_set_led, led_number = led_number, state = state))

    def callback_call_set_led(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info(str(response.success))
        except Exception as e:
            self.get_logger().info("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = Battery()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
