
"""Copyright [2017] [Siddhant Mahapatra]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://github.com/Robosid/SLAMBOT/blob/master/License.pdf
    https://github.com/Robosid/SLAMBOT/blob/master/License.rtf

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



'''

CAMERA SETUP CLASS

'''


from picamera.array import PiRGBArray
from picamera import PiCamera

def init():
	camera = PiCamera()
	camera.resolution = (320,240)
	camera.framerate = 30
	camera.sensor_mode = 3
	camera.rotation = 90
	#camera.exposure_compensation = 0
	camera.shutter_speed = camera.exposure_speed
	camera.exposure_mode = 'off'
	#camera.awb_mode = 'off'
	#camera.awb_gains = g
	#camera.contrast = 10
	camera.brightness = 50
	camera.saturation = 50 #brighter colours
	camera.ISO = 100
	rawCapture = PiRGBArray(camera, size=(320,240))
	return (camera, rawCapture)
