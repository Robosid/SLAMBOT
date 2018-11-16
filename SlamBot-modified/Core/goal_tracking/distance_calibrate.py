
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

DISTANCE PIXEL CALIBRATOR CLASS 

'''

import cv2 
import colorBlobDetector as blob

class pixelCalibrate(object):
	
	def __init__(self, knownDistance, knownWidth):

		self.KNOWN_DISTANCE = knownDistance
		self.KNOWN_WIDTH = knownWidth
		self.image_path = 'tools/calibration/opencv_image_0.png'	
		image_calibrate = cv2.imread(self.image_path)
		detectYellow = blob.get_blob('yellow', image_calibrate)
		c_marker = detectYellow.find_marker()	
		self.focalLength = (c_marker[1][0] * knownDistance) / knownWidth
		
	def distance_to_camera(self, perWidth):
		return (self.KNOWN_WIDTH * self.focalLength) / perWidth
	
