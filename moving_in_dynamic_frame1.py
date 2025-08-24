from pyniryo import *
import time

# - Constants
workspace_name = "tic_tac_wspace"  # Robot's Workspace Name
robot_ip_address = "192.168.68.107"
robot = NiryoRobot(robot_ip_address)
# Calibrate robot if the robot needs calibration
robot.calibrate_auto()
# Updating tool
robot.update_tool()

# robot.move_relative([-0.05, 0, 0, 0, 0, 0], frame="dynamic_frame1")

robot.move_linear_relative([0, 0, 0.05, 0, 0, 0], frame="dynamic_frame1")


robot.close_connection()