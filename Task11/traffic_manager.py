import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import math

class traffic_manager(Node):
    def __init__(self):
        super().__init__('traffic_manager')

        self.first_sub = self.create_subscription(Pose2D, 'fleet_position', self.position_callback, 10)
        self.second_sub = self.create_subscription(Int32, 'fleet_priority', self.priority_callback, 10)

        self.my_x = 100.0
        self.my_y = 100.0
        self.my_pri = 3
        self.safety_zone = 2.0

        self.other_x = None
        self.other_y = None
        self.other_priority = None

    def priority_callback(self, msg:Int32):
        self.other_priority = msg.data

    def position_callback(self, msg:Pose2D):
        self.other_x = msg.x
        self.other_y = msg.y

        if self.other_priority is not None and self.other_x is not None:
            self.check_traffic()

    def check_traffic(self):
        dx = self.my_x - self.other_x
        dy = self.my_y - self.other_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance <= self.safety_zone and self.other_priority > self.my_pri:
            self.get_logger().warn(f"DANGER")
        else:
            self.get_logger().info(f"CLEAR")

def main(args=None):
    rclpy.init(args=args)
    node = traffic_manager()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


