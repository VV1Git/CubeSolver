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

 
bluePins = [26, 19, 13, 6]

blue = RpiMotorLib.BYJMotor("Blue", "Nema")
time.sleep(0.5)

# GPIO Pins, wait, steps, counterclockwise, verbose, steptype ("full, half, wave"), initdelay - 50 steps per rotation on half
# Black -> Out3
# Green -> Out1
# Red -> Out4
# Blue -> Out2
blue.motor_run(bluePins, 0.01, 5000, False, False, "full", .05)