from pyniryo import *
import keyboard
from pprint import pprint
import time
import pickle
import json

# - Constants
robot_ip_address = "192.168.68.106"
robot = NiryoRobot(robot_ip_address)
# Calibrate robot if the robot needs calibration
robot.calibrate_auto()
# Updating tool
robot.update_tool()

traj_li = []

robot.set_learning_mode(True)

circle = {
    "top_left" : [],
    "top_right" : [],
    "bottom_left" : [],
    "bottom_right" : []
}


while 1:
    a = input("Enter the command: ")
    
    if a == 'tl':
        circle['top_left'] = robot.get_pose()
    if a == 'tr':
        circle['top_right'] = robot.get_pose()
    if a == 'bl':
        circle['bottom_left'] = robot.get_pose()
    if a == 'br':
        circle['bottom_right'] = robot.get_pose()

    if a == 'exit':
        robot.set_learning_mode(False)

        with open('circle.json', 'w') as json_file:
            json.dump(circle, json_file)  

        print(circle["top_left"])
        print(circle["top_right"])
        print(circle['bottom_left'])
        print(circle['bottom_right'])
        break

with open('circle.json', 'r') as json_file:
    circle = json.load(json_file)

print(circle)

center_x = (circle['top_left'].x + circle['bottom_right'].x)/2
center_y = (circle['top_left'].y + circle['bottom_right'].y)/2


x = 0
y = 0





#robot.execute_trajectory_from_poses(new_li, dist_smoothing= 1.0)


robot.close_connection()