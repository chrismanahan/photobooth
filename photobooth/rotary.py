from RPi import GPIO
from time import sleep

class Rotary:
	
	def __init__(self, clkPin, dtPin, upperBound):
		print("setting up rotary")
		GPIO.setup(clkPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(dtPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self.counter = 0
		self.upperBound = upperBound
		self.callback = None
		self.clkLastState = GPIO.input(clkPin)
		self.clkPin = clkPin
		self.dtPin = dtPin
		GPIO.add_event_detect(clkPin, GPIO.FALLING, callback=self._run, bouncetime=1)
		
	def getValue(self):
		return self.counter % (self.upperBound + 1)
		
	def registerCallback(self, func):
		print("registering callback with rotary")
		self.callback = func
		
	def clearCallback(self):
		print("clearing callback with rotary")
		self.callback = None
		
	def _run(self, args):
		print("run rotary")
		#if self.callback == None:
		#	return
		try:
			clkState = GPIO.input(self.clkPin)
			dtState = GPIO.input(self.dtPin)
			print("\tclk: " + str(clkState))
			print("\tdt: " + str(dtState))
			if clkState != self.clkLastState:
				print("update rotary")
				if dtState != clkState:
					self.counter += 1
				else:
					self.counter -= 1
				print("count: " + str(self.counter))
				#self.callback(self.getValue())
			else:
				print("dont update rotary")
			self.clkLastState = clkState
		finally:
			pass
