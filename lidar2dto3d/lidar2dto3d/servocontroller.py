import rclpy
from gpiozero import AngularServo
from std_msgs.msg import Float32
from rclpy.node import Node

class AngleSetpointSubscriber(Node):
    def __init__(self, pin):
        super().__init__('anglesetpoint_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'anglesetpoint',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # use GPIO pin for the servo control
        self.pin = pin

        # Define the servo motor's minimum and maximum pulse widths
        self.MIN_PULSE_WIDTH = 0.00054  # 540 µs
        self.MAX_PULSE_WIDTH = 0.00247  # 2470 µs

        # Create a Servo object for GPIO pin
        self.servo = AngularServo(self.pin, min_pulse_width=self.MIN_PULSE_WIDTH, max_pulse_width=self.MAX_PULSE_WIDTH)

    def listener_callback(self, msg):
        self.servo.angle = msg.data
        self.get_logger().info('Servo angle: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    try:
        # use GPIO pin 18 for the servo control
        pin = 18
        anglesetpoint_subscriber = AngleSetpointSubscriber(pin)
        rclpy.spin(anglesetpoint_subscriber)
    except KeyboardInterrupt:
        pass

    # Stop the servo
    servo.detach()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    angle_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
