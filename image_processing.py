from pyniryo import *
import pprint
import cv2
import pyautogui

observation_pose = [0.214, -0.016, 0.253, -0.282, 1.462, -0.592]

# Connecting to robot
robot = NiryoRobot("192.168.68.107")
robot.calibrate_auto()

# Getting calibration param
mtx, dist = robot.get_camera_intrinsics()
print(mtx)
print(dist)

# Moving to observation pose
robot.move_pose(observation_pose)
cap = cv2.VideoCapture(0)
while "User do not press Escape neither Q":
    ret, frame = cap.read()
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert('RGB')

    # Getting image
    img_compressed = robot.get_img_compressed()
    # Uncompressing image
    img_raw = uncompress_image(img_compressed)
    # Undistorting
    img_undistort = undistort_image(img_raw, mtx, dist)

    # - Display
    # Concatenating raw image and undistorted image
    concat_ims = concat_imgs((img_raw, img_undistort,frame))

    # Showing images
    key = show_img("Images raw & undistorted", concat_ims, wait_ms=30)
    if key in [27, ord("q")]:  # Will break loop if the user press Escape or Q
        break


robot.close_connection()