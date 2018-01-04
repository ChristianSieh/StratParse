import json
import logClass

def readFile(filename):
	with open(filename, 'r') as logfile:
		data = logfile.read()
	logfile.closed

	logs = data.split(';')

	return logs

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
		print(body)
		if(body != "\n"):
			tempData.append(body)

	return myLog, tempData

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
				data[key] = value
		log.body.append(data)

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
#for log in logList:
	#log.printTestLog()

