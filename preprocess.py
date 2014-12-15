import pandas as pd

data = []

with open("data.txt", "r") as f:
	for line in f:
		data.append(line.split())


currentVal = "0"
sensorValues = []	# list of segmented sensor readings
y = []
event = []
Xheader = ["AcX", "AcY", "AcZ", "GyX", "GyY", "GyZ"]
Yheader = ["labels"]


for row in data[1:]:
	print 
	if row[0] == currentVal:
		event.append(row[1:])
	else:
		if row[0] == "1":
			sensorValues.append(event)
			y.append(0)
		if row[0] == "0":
			sensorValues.append(event)
			y.append(1)
		currentVal = row[0]
		event = []


def feature_extract(segment):
	AcX = [row[0] for row in segment]
	AcY = [row[1] for row in segment]
	AcZ = [row[2] for row in segment]
	GyX = [row[3] for row in segment]
	GyY = [row[4] for row in segment]
	GyZ = [row[5] for row in segment]
	AcXmean = sum(AcX) / len(AcX)
	AcYmean = sum(AcY) / len(AcY)
	AcZmean = sum(AcZ) / len(AcZ)
	GyXmean = sum(GyX) / len(GyX)
	GyYmean = sum(GyY) / len(GyY)
	GyZmean = sum(GyZ) / len(GyZ)
	AcYvariance = 
	AcZvariance = 
	GyXvariance = 
	GyYvariance = 
	GyZvariance = 
	# mean for each reading (6)
	# variance for each reading (6)