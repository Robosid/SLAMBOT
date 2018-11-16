
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



#!usr/bin/python3

'''

MOTOR CONTROLLER CLASS

'''

import math
import penguinPi as ppi

mA = ppi.Motor(ppi.AD_MOTOR_A)
mB = ppi.Motor(ppi.AD_MOTOR_B)

def init():
	ppi.init()
	driveMotors(0,0)
		
def driveMotors(speedA, speedB):

	mA.set_power(-speedA)
	mB.set_power(speedB)
	
def get_ticksA():
	return mA.get_ticks()
	
def get_ticksB():
	return mB.get_ticks()

class get_distance(object):
	def __init__(self, ticksA, ticksB):
		#Need to find real full revolution ticks value was just a guess
		self.distA = ((ticksA / 360) * (math.pi * 65)) #convert ticks to meters
		self.distB = ((ticksB / 90) * (math.pi * 65)) #convert ticks to meters
		#self.distA = ticksA
		#self.distB = ticksB
		
	def return_distanceA(self):
		return self.distA
		
	def return_distanceB(self):
		return self.distB
		
		
