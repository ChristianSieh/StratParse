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
	#TODO strip bodies of ending }

	#Get the header line with everything split apart
	header = bodies[0].strip().split(' ')

	#Assign action, header type, and header subtype
	myLog.action = header[0]
	temp = header[1].split('(')
	myLog.headerType = temp[0]
	myLog.headerSubType = temp[1].replace(')', '')

	return myLog

#Read file
logs = readFile("Sample-stratasys-status-log.txt")

#TODO fix extra log entry or just use pop
logs.pop()

logList = []

#Parse each log in logs
for log in logs:
	logList.append(parseLog(log))

#Print logs
for log in logList:
	log.printTestLog()

