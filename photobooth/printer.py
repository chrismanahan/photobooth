import cups
from enum import Enum
import os

class PrinterState(Enum):
	READY = 3
	PRINTING = 4
	ERROR = 5

class Printer:
	def __init__(self):
		self.conn = cups.Connection()
		printers = self.conn.getPrinters()
		self.printerName = list(printers.keys())[0]
		
	def printFile(self, filename, count = 1):
		cmd = "lp -d " + self.printerName + " -n " + str(count) + " " + filename
		print("\nrunning cmd:" + cmd)
		os.popen(cmd)
		print("\nprinting " + filename) 

	def getState(self):
		att = self._getAttributes()
		return PrinterState(att['printer-state'])
		
	def getErrorMessage(self):
		return self._getAttributes()['printer-state-message']
		
	def _getAttributes(self):
		return self.conn.getAttributes(printerName)
