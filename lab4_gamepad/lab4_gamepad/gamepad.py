#!/usr/bin/env python3
# The above line is a shebang, which tells the system to run this script using Python 3.
 
# Import necessary ROS 2 libraries
import rclpy  # ROS 2 client library for Python
from rclpy.node import Node  # Base class for creating ROS 2 nodes
 
# Import message types
from sensor_msgs.msg import Joy  # Message type for joystick (gamepad) inputs
from geometry_msgs.msg import Twist  # Message type for velocity commands
 
class Gamepad(Node):
    """
    A ROS 2 Node that converts joystick (gamepad) inputs into velocity commands
    for a robot. It subscribes to the 'joy' topic and publishes Twist messages
    to the 'cmd_vel' topic.
    """
    def __init__(self):
        """
        Constructor: Initializes the gamepad node.
        - Subscribes to the 'joy' topic to receive joystick inputs.
        - Publishes to the 'cmd_vel' topic to send velocity commands.
        """
        # TODO: Initialize the node with the name 'gamepad'
        super().__init__('gamepad')
 
        # TODO: Create a subscriber to the 'joy' topic (gamepad inputs)
        # - This listens for messages of type Joy.
        # - It calls the `joy_callback` function whenever a new message arrives.
        # - Queue size of 10 will buffer up to 10 messages before discarding old ones.
        self.subscription = self.create_subscription(Joy,'joy', self.joy_callback, 10)
 
        # TODO: Create a publisher to send velocity commands to the 'cmd_vel' topic.
        # - This sends messages of type Twist.
        # - Queue size of 10 helps manage message buffering.
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
 
        # Log a message indicating that the node has started successfully
        self.get_logger().info("Joy to cmd_vel node started!")
 
    def joy_callback(self, msg):
        """
        Callback function that processes incoming joystick messages.
        - Extracts axis values from the joystick message.
        - Converts these values into a Twist message (velocity commands).
        - Publishes the Twist message to control the robot.
 
        Args:
            msg (Joy): The incoming joystick message containing axes and button states.
        """
        # TODO: Create a new Twist message (velocity command)
        Tmsg = Twist()
 
        # TODO: Map joystick axes to robot velocity:
        # The left stick up/down controls linear speed (forward/backward)
        # The right stick left/right controls angular speed (rotation)
        Tmsg.linear.x = msg.axes[1]*0.22
        Tmsg.angular.z = msg.axes[3]*2.8
 
        # TODO: Publish the velocity command to the 'cmd_vel' topic
        self.publisher_.publish(Tmsg)
 
def main(args=None):
    """
    Main function to start the ROS 2 node.
    - Initializes the ROS 2 system.
    - Creates an instance of the Gamepad node.
    - Keeps the node running using `rclpy.spin()`, which listens for messages.
    - Cleans up resources when the node is shut down.
    """
    rclpy.init(args=args)  # Initialize ROS 2
    gamepad = Gamepad()  # Create an instance of the Gamepad node
    rclpy.spin(gamepad)  # Keep the node running and responsive to joystick input
 
    # Cleanup when the node is shutting down
    gamepad.destroy_node()  # Properly destroy the node
    rclpy.shutdown()  # Shutdown ROS 2
 
# Run the script if executed directly (not imported as a module)
if __name__ == '__main__':
    main()