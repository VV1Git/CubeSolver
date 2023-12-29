import numpy as np
from picamera import PiCamera
from time import sleep
print("started")
camera = PiCamera()
camera.iso = 200
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
camera.resolution = (1024, 768)
#camera.exposure_mode = 'auto'
#camera.awb_mode = 'auto'
camera.start_preview()
sleep(2)
camera.capture('image1.jpg')
camera.close()