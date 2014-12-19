import serial
import time


"""
	changed setup: now only using one arduino, but two breadboards:
		(1) user breadboard and (2) caretaker breadboard
"""


def read_fsr():
	ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
	while True:
		val = int(ser.readline())
		if val == 1:
			ser.write("1")
		if val == 2:
			ser.write("2")
		time.sleep(1)
