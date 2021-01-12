import os
import picamera
from PIL import Image
from time import sleep

# Env variables
os.environ['resolution'] = '3280x2464'
os.environ['framerate'] = '15'
os.environ['output_location'] = '/media/pi/CONFIG'

# Camera Init
camera = picamera.PiCamera()
camera.resolution = os.environ.get('resolution')
camera.framerate = os.environ.get('framerate')
camera.start_preview()

# Camera warm-up time
sleep(2)
for counter in range(5):
    print(counter)
    camera.capture_continuous('{path}/image{counter}.jpg'.format(path=os.environ.get('output_location'))

# Wait indefinitely until the user terminates the script
while True:
  sleep(1)