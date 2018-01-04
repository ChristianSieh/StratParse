import json
import logClass

#Read specified file
def readFile(filename):
	with open(filename, 'r') as logfile:
		data = logfile.read()
	logfile.closed

	logs = data.split(';')

	return logs

#Check if string is an int
def isInt(num):
	try:
		num = int(num)
		return True
	except ValueError:
		return False

#Check if string is a float
def isFloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

#Seperate header and bodies
def parseLog(log):
	myLog = logClass.logClass()

	bodies = log.split("{\n")

	#Get the header line with everything split apart
	header = bodies[0].strip().split(' ')

	#Assign action, header type, and header subtype
	myLog.action = header[0]
	temp = header[1].split('(')
	myLog.headerType = temp[0]
	myLog.headerSubType = temp[1].replace(')', '')

	#Remove header since we no longer need it
	bodies.pop(0)

	tempData = []

	#Push bodies into tempData to be parsed later
	#TODO fix extra }
	for body in bodies:
		body = body.strip()
		body = body.rstrip('}')
		if(body != "\n"):
			tempData.append(body)

	return myLog, tempData

#Parses the body of each log
def parseData(log, tempData):
	for body in tempData:
		lines = body.splitlines()
		data = {}
		for line in lines:
			line = line.strip().strip('-')
			if(line != "}"):
				temp = line.split(' ', 1)
				key = temp[0]
				value = temp[1]
				data[key] = parseValue(value)
		log.body.append(data)

#Parse the values of each key to determine data type
def parseValue(value):
	#TODO Finish splitting lists		
	#If list (by checking brackets)
		#If brackets then check if empty
		#Elif check if datetime (Use library parser?)
		#Else split and check if int, float, string
	#else
		#Check if int, float, string
	if('{' in value):
		value.replace('{', '').replace('}', '')
		if(value.isspace()):
			temp = []
			return temp
		#elif():
		#else:
			
	else:
		if(isFloat(value)):
			if(isInt(value)):
				return int(value)
			else:
				return float(value)
		else:
				return value		

#Read file
logs = readFile("Sample-stratasys-status-log.txt")

#TODO fix extra log entry or just use pop
logs.pop()

logList = []

#Parse each log in logs
for log in logs:
	myLog, test = parseLog(log)
	parseData(myLog, test)
	logList.append(myLog)

#Print logs
for log in logList:
	log.printTestLog()

