import os
import picamera
from PIL import Image
from time import sleep

# Env variables
os.environ['resolution'] = '3280x2464'
os.environ['output_location'] = '/media/pi/CONFIG'
os.environ['session_limit'] = '5'

# Methods
def setupCamera():
  print('Camera starting...')
  camera = picamera.PiCamera()
  camera.resolution = os.environ.get('resolution')
  camera.start_preview()
  #sleep(2)
  #return camera

def startSequence(camera):
  counter = 0
  for filename in camera.capture_continuous(str(os.environ.get('output_location')) + '/image{counter}.jpg'):
    counter += 1
    if (counter != int(os.environ['session_limit'])):
      print(filename)
    else:
      break

def endSession(camera):
  camera.close()
  print('Complete')

# Start camera sequence
camera = setupCamera()
#startSequence(camera)
#endSession(camera)
