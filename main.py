import numpy as np
from picamera import PiCamera
print("started")
camera = PiCamera()
print(camera.iso)
camera.capture('image0.jpg')
camera.iso = 800
camera.capture('image1.jpg')
print(camera.iso)