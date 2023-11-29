#!/usr/bin/env python

import rclpy
import RPi.GPIO as GPIO
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import math

GPIO.setmode(GPIO.BOARD)
servo_pin = 18  # Change this to the actual GPIO pin connected to your servo
lidar_frame_id = "lidar_frame"
base_link_frame_id = "base_link"

GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency

def servo_callback(data):
    # Convert the angle (in degrees) from the message to the duty cycle
    angle = data.data
    duty_cycle = angle / 18.0 + 2.5
    servo.ChangeDutyCycle(duty_cycle)

def lidar_callback(scan):
    # Create a transform
    t = TransformStamped()
    t.header.stamp = rclpy.Time.now()
    t.header.frame_id = base_link_frame_id
    t.child_frame_id = lidar_frame_id
    t.transform.translation.x = 0.0  # Adjust these values based on your setup
    t.transform.translation.y = 0.0
    t.transform.translation.z = 0.0
    t.transform.rotation.x = 0.0
    t.transform.rotation.y = 0.0
    t.transform.rotation.z = 0.0
    t.transform.rotation.w = 1.0

    # Broadcast the transform
    br = TransformBroadcaster()
    br.sendTransform(t)

    # Get the current servo angle
    servo_angle = rclpy.get_param('servo_angle', 0.0)

    # Adjust the lidar scan based on the servo angle
    adjusted_ranges = []
    for i, r in enumerate(scan.ranges):
        angle = scan.angle_min + i * scan.angle_increment
        adjusted_angle = angle + math.radians(servo_angle)
        adjusted_ranges.append(r * math.cos(adjusted_angle))  # Adjust the range based on the angle

    # Publish the adjusted scan
    adjusted_scan = scan
    adjusted_scan.header.frame_id = base_link_frame_id
    adjusted_scan.ranges = adjusted_ranges
    pub.publish(adjusted_scan)

def servo_control_node():
    rclpy.init_node('servo_control_node', anonymous=True)
    rclpy.Subscriber('servo_angle', Float64, servo_callback)
    rclpy.Subscriber('/scan', LaserScan, lidar_callback)
    rclpy.spin()

if __name__ == '__main__':
    try:
        servo_control_node()
    except rclpy.ROSInterruptException:
        pass
    finally:
        GPIO.cleanup()
