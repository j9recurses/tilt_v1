import numpy as np
import pandas as pd
from sklearn import linear_model as lm
import serial
import pickle



def feature_extract(segment):
	""" Input: A slice of sensor data stream; list of lists ([ [s1,s2,s3,s4,s5,s6], ...  ]) [114 X 6]
		Output: np array feature matrix
	"""
	array = np.array(segment).astype(float)
	m = np.mean(array, 0)    # returns an array of means
	v = np.var(array, 0)     # returns an array of variances
	features = np.append(m,v)    # creates a [1 X 12] array
	return features

def main(classifier, feature_function):
	ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
	i = 0
	window = 100
	windowList = []

	# get rid of first 20 sensor readings; these tend to be buggy
	while i < 20:
		ser.readline()
		i += 1


	while True:
		windowList.append(ser.readline().split()[1:])    
		# split sensor reading into a list and append list to windowList
		# first item in list is fsr_reading label [0,1] which is not needed
		if len(windowList) >= window:
			sample = windowList[:window]    # take first 100 readings
			predict = classifier.predict(feature_function(sample))
			if predict.item(0) == 1:			# 'predict' is a numpy ndarray object
				windowList = []
			else:
				del windowList[:(window / 2)]         # overlap readings by 50%
			print "Prediction: ", predict.item(0)





if __name__ == "__main__":
	clf = pickle.load(open("LG_Classifier.p", "rb"))
	main(clf, feature_extract)


