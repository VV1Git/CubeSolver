import numpy as np
from picamera import PiCamera
print("started")
camera = PiCamera()
camera.capture('image.jpg')
print(camera.ISO)