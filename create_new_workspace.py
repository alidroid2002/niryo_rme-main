from pyniryo import *


robot_ip_address = "192.168.68.107"

# - Initialization

# Connect to robot
robot = NiryoRobot(robot_ip_address)
# Calibrate robot if the robot needs calibration
robot.calibrate_auto()
# Updating tool
robot.update_tool()

robot.set_learning_mode(True)

c = input("Go to origin: ")
pose_o = robot.get_pose()

c = input("Go to pose 2 : ")
pose_2 = robot.get_pose()

c = input("Go to pose 3 : ")
pose_3 = robot.get_pose()

c = input("Go to pose 4 : ")
pose_4 = robot.get_pose()

robot.save_workspace_from_robot_poses("asymmetric_workspace",pose_o, pose_2, pose_3, pose_4)

robot.set_learning_mode(False)

print(robot.get_workspace_list())

robot.close_connection()