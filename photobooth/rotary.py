from RPi import GPIO
from time import sleep

class Rotary:
	
	def __init__(self, clkPin, dtPin, upperBound):
		print("setting up rotary")
		GPIO.setup(clkPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(dtPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self.resetCount()
		self.upperBound = upperBound
		self.callback = None
		self.clkLastState = GPIO.input(clkPin)
		self.clkPin = clkPin
		self.dtPin = dtPin
		GPIO.add_event_detect(clkPin, GPIO.FALLING, callback=self._run, bouncetime=500)
		
	def getValue(self):
		return self.counter	
	
	def registerCallback(self, func):
		print("registering callback with rotary")
		self.callback = func
		
	def clearCallback(self):
		print("clearing callback with rotary")
		self.callback = None
		
	def resetCount(self):
		self.counter = 1
		
	def _run(self, pin):
		print("run rotary")
		if self.callback == None:
			return
		try:
			clkState = GPIO.input(self.clkPin)
			dtState = GPIO.input(self.dtPin)
			if dtState != clkState:
				self.counter += 1
			else:
				self.counter -= 1
				
			self._boundCounter()
			self.callback(self.counter)
		finally:
			pass

	def _boundCounter(self):
		if self.counter > self.upperBound:
			self.counter = 1
		elif self.counter < 1:
			self.counter = self.upperBound
