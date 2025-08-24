from pyniryo import *
import keyboard
from pprint import pprint
import time
import pickle

# - Constants
robot_ip_address = "192.168.68.106"
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
        traj_li.append(robot.get_pose())

    if a == 'run':
        break

    if a == 'exit':
        with open('traj_li1.pkl', 'wb') as f:
            pickle.dump(traj_li, f)
        robot.set_learning_mode(False)
        break


pprint(traj_li, width=1)
robot.set_arm_max_velocity(percentage_speed= 100)
time.sleep(3)

load_traj_li = []

with open('traj_li1.pkl', 'rb') as f:
    load_traj_li = pickle.load(f)

new_li = []
for li in load_traj_li:
    new_li.append([li.x, li.y, li.z, li.roll, li.pitch, li.yaw])
    #print(li.x)


for li in new_li:
    print(li)


robot.execute_trajectory_from_poses(new_li, dist_smoothing= 1.0)

for li in load_traj_li:
    robot.move_pose(li)

robot.close_connection()