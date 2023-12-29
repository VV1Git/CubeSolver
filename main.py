import numpy as np
from picamera import PiCamera
print("started")
camera = PiCamera()
print(camera.ISO)
camera.capture('image0.jpg')
camera.ISO = 800
camera.capture('image1.jpg')
print(camera.ISO)