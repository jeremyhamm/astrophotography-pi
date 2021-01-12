import os
import picamera
from PIL import Image
from time import sleep

# Env variables
os.environ['resolution'] = '3280x2464'
os.environ['output_location'] = '/media/pi/CONFIG'
os.environ['session_limit'] = '5'

# Camera Init
camera = picamera.PiCamera()
camera.resolution = os.environ.get('resolution')
camera.start_preview()

# Camera warm-up time
print('Camera starting...')
sleep(2)
counter = 0
for filename in camera.capture_continuous(str(os.environ.get('output_location')) + '/image{counter}.jpg'):
  counter += 1
  if (counter != int(os.environ['session_limit'])):
    print(str(os.environ.get('output_location')) + 'image{counter}.jpg')
  else:
    break

camera.close()
print('Complete')