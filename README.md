# Finger-counter using OpenCV
A computer vision project made using OpenCV(Python) and mediapipe libraries. It counts the number of fingers in the video captured by the webcam/video given.

# Requirements
* OpenCV
* Python 3.7+
* mediapipe

# About Project
* The Handtracker file consists of a class Handdetector
* The class has two class methods for detecting hands i.e. findHands and for finding the positional landmarks i.e. findPosition 
* The FingerCounter file contains the module to capture the video through webcam and count the number of fingers. The tip ids can be seen in the pic below

![landmark](https://github.com/ChiragChauhan4579/Finger-counter/blob/main/hand_landmarks.png)

![finger-counter](https://github.com/ChiragChauhan4579/Finger-counter/blob/main/Video.gif)
