# Stereo-Camera-Calibration
This is for calibrating stereo camera systems with radial or barrel lens distortion, and returning a corrected image with no distortion. To do so, you must take pictures of a 8x5 checkerboard at various positions with uncalibrated_camera.py. Other board dimensions work, but values must be changed accordingly. 

# uncalibrated_camera.py
This file opens the camera as it is, with distortion present in order to take images that will be calibrated later to create the calibrated video as well as to create a depth map. Press 'q' to quit and 's' to take a picture.

# fundamental_matrix.py
After taking several pictures (10 or more) with uncalibrated_camera.py, run this to generate the fundamental matrixes for the left and right cameras. Then the subsequent values
will be saved in a npz file for use in calibrated_camera.py.

# calibrated-camera.py
calibrated_camera.py shows the undistorted live video from the camera. It does so by taking the matrix values from fundamental_matrix.py and corrrecting them.

# undistort_picture.py
This takes a distorted jpg, undistorts it, and returns it as a png for use in a depth map.

# depth_map.py
To be added
