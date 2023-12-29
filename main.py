import numpy as np
from picamera import PiCamera
print("started")
camera = PiCamera()
camera.contrast = 50
camera.capture('image1.jpg')
camera.close()