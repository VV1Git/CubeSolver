#import numpy as np
#from picamera import PiCamera
#import kociemba
import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib


"""kociemba.solve('UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB')
print("started")
camera = PiCamera()
camera.iso = 200
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
camera.led = False
camera.resolution = (1024, 768)
camera.exposure_mode = 'auto'
camera.awb_mode = 'auto'
camera.start_preview()
sleep(2)
camera.capture('image1.jpg')
camera.close()"""

 
yellowPins = [26, 19, 13, 6]
redPins = [5, 11, 9, 10]
greenPins = [22, 27, 17, 4]

yellow = RpiMotorLib.BYJMotor("Yello", "Nema")
red = RpiMotorLib.BYJMotor("Red", "Nema")
green = RpiMotorLib.BYJMotor("Green", "Nema")
time.sleep(0.5)

steptype = "full"
initdelay = .05


# GPIO Pins, wait, steps, counterclockwise, verbose, steptype ("full, half, wave"), initdelay - 50 steps per rotation
for i in range(3):
    green.motor_run(greenPins, 0.001, 50//4, False, False, steptype, initdelay)
    yellow.motor_run(yellowPins, 0.001, 50//4, False, False, steptype, initdelay)
    green.motor_run(greenPins, 0.001, 50//4, True, False, steptype, initdelay)
    red.motor_run(redPins, 0.001, 50//4, True, False, steptype, initdelay)
    green.motor_run(greenPins, 0.001, 50//4, False, False, steptype, initdelay)
    yellow.motor_run(yellowPins, 0.001, 50//4, False, False, steptype, initdelay)
    green.motor_run(greenPins, 0.001, 50//4, True, False, steptype, initdelay)
    yellow.motor_run(yellowPins, 0.001, 50//4, True, False, steptype, initdelay)
    green.motor_run(greenPins, 0.001, 50//4, True, False, steptype, initdelay)
    red.motor_run(redPins, 0.001, 50//4, False, False, steptype, initdelay)
    green.motor_run(greenPins, 0.001, 25, False, False, steptype, initdelay)
    yellow.motor_run(yellowPins, 0.001, 50//4, True, False, steptype, initdelay)
    green.motor_run(greenPins, 0.001, 50//4, True, False, steptype, initdelay)