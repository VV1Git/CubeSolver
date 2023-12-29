import numpy as np
from picamera import PiCamera
print("Hello World!")
print(np.__version__)
camera = PiCamera()
camera.capture('image.jpg')