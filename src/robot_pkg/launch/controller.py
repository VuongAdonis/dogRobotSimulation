import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class DogRobotController(Node):
    def __init__(self):
        super().__init__('dog_robot_controller')

        self.publisher = self.create_publisher(Float64, '/front_left_leg_position_controller/commands', 10)

        # Vòng lặp để điều khiển góc
        self.timer = self.create_timer(0.1, self.move_leg)

    def move_leg(self):
        msg = Float64()
        msg.data = 0.5  # Thay đổi giá trị cho chuyển động
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    controller = DogRobotController()
    rclpy.spin(controller)

    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
