import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

class fleetsimulator(Node):
    def __init__(self):
        super().__init__('fleet_simulator')
        self.first_publisher = self.create_publisher(Pose2D, 'fleet_position', 10)
        self.second_publisher = self.create_publisher(Int32, 'fleet_priority', 10)

        self.timer = self.create_timer(0.1, self.broadcast_status)

        self.x = 0.0
        self.y = 0.0
        self.robot_priority = 5

    def broadcast_status(self):
        self.x += 0.1
        self.y += 0.1

        pos_msg = Pose2D()
        pos_msg.x = self.x
        pos_msg.y = self.y
        pos_msg.theta = 0.0

        pri_msg = Int32()
        pri_msg.data = self.robot_priority

        self.first_publisher.publish(pos_msg)
        self.second_publisher.publish(pri_msg)

        self.get_logger().info(f"Position: ({pos_msg.x:.1f},{pos_msg.y:.1f}), Priority: {pri_msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = fleetsimulator()     #to create node
    rclpy.spin(node)            #to use node (While loop)
    rclpy.shutdown()            #to kill node

if __name__ == '__main__':
    main()