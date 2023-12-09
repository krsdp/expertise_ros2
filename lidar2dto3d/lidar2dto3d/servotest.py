from gpiozero import Servo
from time import sleep

# Define the servo motor's minimum and maximum pulse widths
MIN_PULSE_WIDTH = 0.00054  # 540 µs
MAX_PULSE_WIDTH = 0.00247  # 2470 µs

# Create a Servo object for GPIO pin 18
servo = Servo(18, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH)

# Move the servo to its minimum position
servo.min()
sleep(1)



# Stop the servo
servo.detach()

def servo_callback(msg):
    # Set the servo angle based on the received message
    servo.angle = msg.data

def main():
    # Initialize the ROS2 node
    rclpy.init()

    # Create a Servo object for GPIO pin 18
    servo = AngularServo(18)

    # Create a ROS2 node
    node = rclpy.create_node('servo_controller')

    # Create a subscriber to listen to the /servoangle topic
    subscriber = node.create_subscription(Float32, '/servoangle', servo_callback)

    # Spin the node to receive messages
    rclpy.spin(node)

    # Clean up
    servo.detach()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

def main():



    # Create a Servo object for GPIO pin 18
    servo = AngularServo(18, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH)

    while True:
        # Sway the servo to +30 degrees
        servo.angle = 90
        sleep(0.7)

        # Sway the servo to -30 degrees
        servo.angle = -90
        sleep(0.7)
    
    servo.detach()
