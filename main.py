import numpy as np
from picamera import PiCamera
print("started")
camera = PiCamera()
camera.exposure_mode = "verylong"
camera.capture('image1.jpg')
camera.close()