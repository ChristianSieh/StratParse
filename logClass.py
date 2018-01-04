class logClass:
	action = ""
	headerType = ""
	headerSubType = ""
	data = ""

	def printTestLog(self):
		print("Action: ", self.action, type(self.action))
		print("Type: ", self.headerType, type(self.headerType))
		print("SubType: ", self.headerSubType, type(self.headerSubType))
