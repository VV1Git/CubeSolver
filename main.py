import numpy as np
from picamera import PiCamera
print("started")
camera = PiCamera()
print(camera.ISO)
camera.ISO = 800
camera.capture('image.jpg')
print(camera.ISO)