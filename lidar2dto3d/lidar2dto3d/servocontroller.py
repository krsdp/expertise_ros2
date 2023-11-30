# servo_controller.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ServoController(Node):
    def __init__(self):
        super().__init__('servo_controller')
        self.servo_publisher = self.create_publisher(Float64, '/servo_position', 10)

    def move_servo(self, position):
        msg = Float64()
        msg.data = position
        self.servo_publisher.publish(msg)
        self.get_logger().info(f'Setting servo position to: {position}')

def main(args=None):
    rclpy.init(args=args)
    servo_controller = ServoController()

    # Set the GPIO pin for the servo
    servo_gpio_pin = 18

    # Set the servo position (replace with your desired values)
    servo_position = 90.0

    # Move the servo to the specified position
    servo_controller.move_servo(servo_position)

    rclpy.spin_once(servo_controller)
    servo_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
