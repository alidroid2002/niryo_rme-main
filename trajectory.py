from pyniryo import *
import keyboard
from pprint import pprint
import time
import pickle

# - Constants
workspace_name = "tic_tac_wspace"  # Robot's Workspace Name
robot_ip_address = "192.168.68.107"
robot = NiryoRobot(robot_ip_address)
# Calibrate robot if the robot needs calibration
robot.calibrate_auto()
# Updating tool
robot.update_tool()

traj_li = []

robot.set_learning_mode(True)

while 1:
    a = input("Enter the command: ")
    
    if a == 'pose':
        traj_li.append(robot.get_pose_quat())

    if a == 'run':
        break

    if a == 'exit':
        with open('traj_li.pkl', 'wb') as f:
            pickle.dump(traj_li, f)
        robot.set_learning_mode(False)
        break


pprint(traj_li, width=1)
time.sleep(3)

with open('traj_li.pkl', 'rb') as f:
    load_traj_li = pickle.load(f)

robot.execute_trajectory_from_poses(load_traj_li, dist_smoothing= -0.0)

robot.close_connection()