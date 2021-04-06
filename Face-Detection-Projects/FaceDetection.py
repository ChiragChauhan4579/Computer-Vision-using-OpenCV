import cv2
import mediapipe as mp
import time

class faceDetector():
    def __init__(self,min_detection_confidence=0.5):
        self.min_detection_confidence = min_detection_confidence
        self.mpface = mp.solutions.face_detection
        self.face = self.mpface.FaceDetection(self.min_detection_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.drawing_spec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findface(self, img, draw=True):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.face.process(img)
        if self.results.detections:
            for faceLms in self.results.detections:
                if draw:
                    self.mpDraw.draw_detection(img, faceLms)
        return img

#######################################
        #For video/webcam#
#######################################
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture('C:/Users/Chirag Chauhan/Downloads/ironman.mp4')
    detector = faceDetector()
    while True:
        success, img = cap.read()
        img = detector.findface(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img,f'FPS:{int(fps)}', (10, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                    (0, 0, 255), 3)

        cv2.imshow('Face-Detector', img)
        k = cv2.waitKey(1)
        if k == 27:
            cv2.destroyAllWindows()


#######################################
             #For image#
#######################################
"""def main():
    detector = faceDetector()
    img = cv2.imread('filname')
    height, width = img.shape[:2]
    img = detector.findface(img)
    cv2.namedWindow('Face-Tracker', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Face-Tracker', width, height)
    cv2.imshow("Face-Tracker", img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
"""
if __name__ == "__main__":
    main()
