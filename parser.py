import json
import logClass

with open("Sample-stratasys-status-log.txt", 'r') as log:
	data = log.read()
log.closed

print(data)
