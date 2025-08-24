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

point_o = []
point_x = []
point_y = []

robot.set_learning_mode(True)

c = input("Go to origin")
o = robot.get_pose_quat()
point_o = o[:3]


c = input("Go to x")
x = robot.get_pose_quat()
point_x = x[0:3]


c = input("Go to y")
y = robot.get_pose_quat()
point_y = y[0:3]

robot.set_learning_mode(False)

print(point_o)
print(point_x)
print(point_y)

robot.save_dynamic_frame_from_points("dynamic_frame1","testing in lab", point_o, point_x, point_y, belong_to_workspace= False)

time.sleep(3)

print(robot.get_saved_dynamic_frame_list())

robot.move_relative([0.05, 0.05, -0.1, 0.3, 0, 0], frame="dynamic_frame1")

##Remember that dynamic frame is saved
robot.close_connection()