from gpiozero import MotionSensor
import time
from datetime import datetime
import cv2
import RPi.GPIO as GPIO

print ("starting motion sensor")
pir =MotionSensor(22)
count =0
while True:
        pir.wait_for_motion()
        count+=1
        print ("motion Detected!" +str(count))
        time.sleep(1)
        
#except KeyboardInterrupt:
#    print ("GPIO.cleanup()")
#    GPIO.cleanup()

        
