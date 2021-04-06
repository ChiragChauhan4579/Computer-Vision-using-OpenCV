# Type of Project:
* [Hand Tracking](https://github.com/ChiragChauhan4579/Computer-Vision-using-OpenCV/blob/main/README.md#hand-tracking)
* [Pose Estimation](https://github.com/ChiragChauhan4579/Computer-Vision-using-OpenCV/blob/main/README.md#pose-estimation)

# Hand Tracking:
* [Finger counter](https://github.com/ChiragChauhan4579/Computer-Vision-using-OpenCV/blob/main/README.md#finger-counter)
* [Volume control using gesture](https://github.com/ChiragChauhan4579/Computer-Vision-using-OpenCV/blob/main/README.md#volume-control-using-gesture)

# Finger counter
This project counts the number of fingers in the video captured by the webcam/video given.

## Requirements
* OpenCV
* Python 3.7+
* mediapipe

## About Project
* The Handtracker file consists of a class Handdetector.
* The class has two class methods for detecting hands i.e. findHands and for finding the positional landmarks i.e. findPosition. 
* The FingerCounter file contains the module to capture the video through webcam and count the number of fingers. The tip ids can be seen in the pic below.

![landmark](https://github.com/ChiragChauhan4579/Computer-Vision-using-OpenCV/blob/main/Hand-Tracking-Projects/hand_landmarks.png)

![finger-counter](https://github.com/ChiragChauhan4579/Computer-Vision-using-OpenCV/blob/main/Hand-Tracking-Projects/Video.gif)


# Volume control using gesture
This project controls the volume using hand gestures.

## Requirements
* OpenCV
* Python 3.7+
* mediapipe
* numpy
* pycaw

## About Project
* The Handtracker file consists of a class Handdetector.
* The class has two class methods for detecting hands i.e. findHands and for finding the positional landmarks i.e. findPosition. 
* The gesture-volume controller file contains the module to control volume using gestures. The pycaw is a library through which we can connect to our audio utilities i.e. to change our volume.
* For all the landmark ids see the image given in finger counter project.

![gesture-control](https://github.com/ChiragChauhan4579/Computer-Vision-using-OpenCV/blob/main/Hand-Tracking-Projects/Video2.gif)

# Pose Estimation
