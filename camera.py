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
print('Camera starting...');
sleep(2)
camera.capture_sequence([
  str(os.environ.get('output_location')) + '/image' + str(counter) + '.jpg' % i
  for i in range(5)
])