import cups

class Printer:
	def __init__(self, printerName):
		self.conn = cups.Connection()
		self.printer = self.conn.getPrinters()[printerName]
		
	def print(self, filename):
		pid = self.conn.printFile(self.printer, filename, filename, {})
		while self.conn.getJobs().get(pid, None) is not None:
			print("printing")
			time.sleep(1)
