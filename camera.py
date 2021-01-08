import picamera
from PIL import Image
from time import sleep

camera = picamera.PiCamera()
camera.resolution = '3280x2464'
camera.framerate = 15
camera.start_preview()

# Camera warm-up time
sleep(2)
camera.capture('/CONFIG/foo.jpg')

# Wait indefinitely until the user terminates the script
while True:
    sleep(1)