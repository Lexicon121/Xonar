import rclpy
from crazyflie_driver.msg import Position


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('takeoff_example')

    publisher = node.create_publisher(Position, 'position', 10)

    msg = Position()
    msg.header.stamp = node.get_clock().now().to_msg()
    msg.x = 0.0
    msg.y = 0.0
    msg.z = 1.0

    i = 0
    while i < 100:
        msg.header.sequence += 1
        publisher.publish(msg)
        i += 1
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
