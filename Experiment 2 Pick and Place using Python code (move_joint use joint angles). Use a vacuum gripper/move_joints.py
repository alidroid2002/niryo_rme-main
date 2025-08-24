from pyniryo import *

robot = NiryoRobot("192.168.68.107")
robot.calibrate_auto()

robot.update_tool()
robot.release_with_tool()
robot.move_joints(0.1, -0.4, 0.3, 0,0, 0)
robot.grasp_with_tool()

robot.close_connection()