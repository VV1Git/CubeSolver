import numpy as np
from picamera import PiCamera
print("started")
camera = PiCamera()
camera.brightness = 90
camera.capture('image1.jpg')
camera.close()