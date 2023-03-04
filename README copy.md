# Xonar Swarm System

This is a general swarm program designed for the Crazyflie 2.0 and ROS2 systems for environment traversal and navigation using the HTC Vive 1.0 lighthouse, Xbox 360 Kinect, and OpenCV

## Prerequisites

- Ubuntu 20.04
- ROS2 Noetic
- Crazyflie Python package: https://github.com/bitcraze/crazyflie-lib-python
- ROS2 repositories: https://github.com/ros2/ros2

To install ROS2 Noetic:

sudo apt update
sudo apt install ros-noetic-desktop

To install the ROS packages for the Crazyflie, the drone, and the Lighthouse:

sudo apt install ros-noetic-crazyflie* ros-noetic-mavros* ros-noetic-vive-ros

Connect the Crazyflie quadcopters and the Lighthouse to your computer via USB and run the following commands to start the ROS drivers:

roslaunch crazyflie_driver crazyflie_usb.launch
roslaunch vive_ros launch_all_vive_nodes.launch

Connect the drone to your computer via USB and run the following command to start the ROS driver:

roslaunch mavros px4.launch fcu_url:=/dev/ttyACM0:921600

Note: Replace /dev/ttyACM0 with the correct port name for your drone.

Prepare the files:

chmod +x Crazyflie Trifecta.py
chmod +x ROS2Takeoff.py

To run Crazyflie Trifecta.py:

python ./Crazyflie Trifecta.py

Note that this is a general overview of the prerequisites for using the Xonar Swarm System. The specifics of each step may vary depending on the hardware and software that you are using. It is important to follow the instructions provided by the hardware and software developers to ensure that you configure and use the devices correctly.
