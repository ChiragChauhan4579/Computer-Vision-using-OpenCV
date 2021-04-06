import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self,min_detection_confidence=0.5):
        self.min_detection_confidence = min_detection_confidence
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.min_detection_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.drawing_spec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findPose(self, img, draw=True):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img)
        if self.results.pose_landmarks:
            poseLms = self.results.pose_landmarks
            self.mpDraw.draw_landmarks(img, poseLms,
                                               self.mpPose.POSE_CONNECTIONS,landmark_drawing_spec=self.drawing_spec,connection_drawing_spec=self.drawing_spec)
        return img

    def findposition(self, img, draw=True):

        lmList = []
        if self.results.pose_landmarks:
            myPose = self.results.pose_landmarks
            for id, lm in enumerate(myPose.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                #if id == 14:
                #    cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList
#######################################
        #For video/webcam#
#######################################
def main():
    pTime = 0
    cTime = 0
    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findposition(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img,f'FPS:{int(fps)}', (10, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                    (0, 0, 255), 3)

        cv2.imshow("Pose-Tracker", img)
        k = cv2.waitKey(1)
        if k == 27:
            cv2.destroyAllWindows()


#######################################
             #For image#
#######################################
"""def main():
    detector = poseDetector()
    img = cv2.imread('filename')
    #height, width = img.shape[:2]
    img = detector.findPosition(img)
    #cv2.namedWindow('Pose-Tracker', cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('Pose-Tracker', width, height)
    cv2.imshow("Pose-Tracker", img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()"""

if __name__ == "__main__":
    main()
