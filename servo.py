import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT) #Connect the servo's positive pin in GPIO pin 37.

pwm = GPIO.PWM(37, 50)
pwm.start(0)

while True:
    pwm.ChangeDutyCycle(1.5)
    sleep(1)
    pwm.ChangeDutyCycle(11.5)
    sleep(2)
GPIO.cleanup()
pwm.stop()
