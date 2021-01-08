import picamera
from PIL import Image
from time import sleep

camera = picamera.PiCamera()
camera.resolution = (3280, 2464)
camera.framerate = 15
camera.start_preview()

# Wait indefinitely until the user terminates the script
while True:
    sleep(1)