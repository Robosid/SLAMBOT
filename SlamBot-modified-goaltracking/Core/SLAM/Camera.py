
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



from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread
import cv2

class PiVideoStream:
	def __init__(self, resolution=(320, 240), framerate=32):
		self.camera = PiCamera()
		self.camera.resolution = resolution
		self.camera.framerate = framerate
		self.camera.sensor_mode = 3
		self.camera.rotation = 90
		self.camera.shutter_speed = self.camera.exposure_speed
		self.camera.exposure_mode = 'off'
		self.camera.brightness = 50
		self.camera.saturation = 50 #brighter colours
		self.camera.ISO = 100
		self.rawCapture = PiRGBArray(self.camera, size=resolution)
		self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)
		self.frame = None
		self.stopped = False
	
	def start(self):
		Thread(target=self.update, args=()).start()
		return self
		
	def update(self):
		for f in self.stream:
			self.frame = f.array
			self.rawCapture.truncate(0)
			
			if self.stopped:
				self.stream.close()
				self.rawCapture.close()
				self.camera.close()
				return
				
	def read(self):
		return self.frame
		
	def stop(self):
		self.stopped = True
		
		
