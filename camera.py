import os
import picamera
from PIL import Image
from time import sleep

# Env variables
os.environ['resolution'] = '3280x2464'
os.environ['output_location'] = '/media/pi/CONFIG'

# Camera Init
camera = picamera.PiCamera()
camera.resolution = os.environ.get('resolution')
camera.start_preview()

# Camera warm-up time
sleep(2)
for counter in range(5):
    print(counter)
    camera.capture_continuous(str(os.environ.get('output_location')) + '/image' + str(counter) + '.jpg')

# Wait indefinitely until the user terminates the script
while True:
  sleep(1)