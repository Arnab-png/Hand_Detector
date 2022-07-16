import RPi.GPIO as GPIO
import time
import cv2
from cvzone.HandTrackingModule import HandDetector

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setwarnings(False)

pwmThumb = GPIO.PWM(11, 50)
pwmIndex = GPIO.PWM(12, 50)
pwmMiddle = GPIO.PWM(13, 50)
pwmRing = GPIO.PWM(15, 50)
pwmPinky = GPIO.PWM(16, 50)

ptime = 0
ctime = 0

detector = HandDetector(detectionCon=0.7, maxHands=1)

video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)

pwmThumb.start(0)
pwmIndex.start(0)
pwmMiddle.start(0)
pwmPinky.start(0)
pwmRing.start(0)

while True :
    success, img = video.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    
    if hands:
        lmlist = hands[0]
        if lmlist:
            fingerUp = detector.fingersUp(lmlist)
            print(fingerUp)
        
        if fingerUp[0] == 0:
            pwmThumb.ChangeDutyCycle(1.5)
            #time.sleep(0.1)
        else:
            pwmThumb.ChangeDutyCycle(11)
            #time.sleep(0.1)
        if fingerUp[1] == 0:
            pwmIndex.ChangeDutyCycle(1.5)
            #time.sleep(0.1)
        else:
            pwmIndex.ChangeDutyCycle(11)
            #time.sleep(0.1)
        if fingerUp[2] == 0:
            pwmMiddle.ChangeDutyCycle(1.5)
            #time.sleep(0.1)
        else:
            pwmMiddle.ChangeDutyCycle(11)
            #time.sleep(0.1)
        if fingerUp[3] == 0:
            pwmRing.ChangeDutyCycle(1.5)
            #time.sleep(0.1)
        else:
            pwmRing.ChangeDutyCycle(11)
            #time.sleep(0.1)
        if fingerUp[4] == 0:
            pwmPinky.ChangeDutyCycle(1.5)
            #ime.sleep(0.1)
        else:
            pwmPinky.ChangeDutyCycle(11)
            #time.sleep(0.1)
    
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    
    cv2.putText(img, str(f'fps:{int(fps)}'),(5,30), cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),1)
    cv2.imshow("Video", img)
    
    if cv2.waitKey(1) & 0xFF==27 :
        break
    
pwmThumb.stop()
pwmIndex.stop()
pwmMiddle.stop()
pwmRing.stop()
pwmPinky.stop()
GPIO.cleanup()
    
video.release()
cv2.destroyAllWindows()