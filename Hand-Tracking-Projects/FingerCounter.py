import cv2
import time
import HandTracker as ht

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = ht.handDetector(detectionCon=0.7)
tipids = [4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []
        if lmList[tipids[0]][1] > lmList[tipids[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1,5):
            if lmList[tipids[id]][2] < lmList[tipids[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalfingers = fingers.count(1)
        print(totalfingers)
        cv2.rectangle(img,(20,225),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(img, str(totalfingers),(25,400),cv2.FONT_HERSHEY_SIMPLEX,7,(255,0,0),10)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'FPS:{int(fps)}',(30,100),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow('Finger Counter',img)
    cv2.waitKey(1)
