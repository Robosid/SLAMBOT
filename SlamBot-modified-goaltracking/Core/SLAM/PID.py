
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

PID CONTROLLER CLASS

'''

class pidcontrol(object):

	def __init__(self, P,I,D):
		self.Kp = P
		self.Ki = I
		self.Kd = D
		self.set_point=0.0
		self.error=0.0
		self.prevError= 0.0
		self.intAccum = 0.0

	def update(self, current_value):
		self.error = self.set_point - current_value
		self.intAccum += self.error
		self.P_value = self.Kp * self.error
		self.D_value = self.Kd * (self.error - self.prevError)
		self.I_value = self.Ki * self.intAccum
		self.prevError = self.error

		Output = self.P_value + self.D_value + self.I_value
		return Output

	def setPoint(self, set_point):
		self.set_point = set_point
