import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MySubscriber(Node):
    def __init__(self, a):
        super().__init__('my_subscriber')
        self.a = a
        self.subscription = self.create_subscription(
            String,
            'my_topic',
            self.callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def callback(self, msg):
        self.get_logger().info('Received message: %s, a: %s' % (msg.data, self.a))

def main(args=None):
    rclpy.init(args=args)
    try:
        a=1
        subscriber = MySubscriber(a)
        rclpy.spin(subscriber)
    except KeyboardInterrupt:
        pass

    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
