import serial
import sys, signal
import time



ser = serial.Serial('/dev/tty.usbmodem1411', 9600)


data = []
# TakingPill == 1 while taking pill
# TakingPill == 0 while not taking pill


i = 0

while i != 10010:
	if i % 1000 == 0:
		print i
	data.append(ser.readline())
	i += 1

del data[:10]

data.insert(0, 'TakingPill AcX AcY AcZ GyX GyY GyZ\n' )
with open("data.txt", "w") as f:
	f.writelines(data)



