class logClass:
	action = ""
	headerType = ""
	headerSubType = ""
	body = []

	def printTestLog(self):
		print("Action: ", self.action)
		print("Type: ", self.headerType)
		print("SubType: ", self.headerSubType)
		for data in self.body:
			for key, value in data.items():
				print("Key: ", key, "Values: ", value, type(value))
