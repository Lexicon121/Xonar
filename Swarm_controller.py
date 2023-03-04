import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from vive_ros.msg import TrackArray
from random import uniform


class SwarmController(Node):
    def __init__(self):
        super().__init__('swarm_controller')
        self.drone_sub = self.create_subscription(
            PoseStamped, '/mavros/local_position/pose', self.drone_callback, 10)
        self.crazyflie_sub = self.create_subscription(
            PoseStamped, '/cf1/pose', self.crazyflie_callback, 10)
        self.lighthouse_sub = self.create_subscription(
            TrackArray, '/trackers', self.lighthouse_callback, 10)
        self.drone_pub = self.create_publisher(
            PoseStamped, '/mavros/setpoint_position/local', 10)
        self.crazyflie_pub = self.create_publisher(
            PoseStamped, '/cf1/cmd_position', 10)

    def drone_callback(self, msg):
        # Implement drone control logic here
        # ...
        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = msg.pose.position.x + uniform(-1, 1)
        pose.pose.position.y = msg.pose.position.y + uniform(-1, 1)
        pose.pose.position.z = msg.pose.position.z + uniform(-1, 1)
        self.drone_pub.publish(pose)

    def crazyflie_callback(self, msg):
        # Implement Crazyflie control logic here
        # ...
        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = msg.pose.position.x + uniform(-0.1, 0.1)
        pose.pose.position.y = msg.pose.position.y + uniform(-0.1, 0.1)
        pose.pose.position.z = msg.pose.position.z + uniform(-0.1, 0.1)
        self.crazyflie_pub.publish(pose)

    def lighthouse_callback(self, msg):
        # Implement Lighthouse obstacle avoidance logic here
        # ...
        pass


def main(args=None):
    rclpy.init(args=args)
    swarm_controller = SwarmController()
    rclpy.spin(swarm_controller)
    swarm_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
