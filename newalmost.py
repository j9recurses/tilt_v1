#!/usr/bin/python

from threading import Thread
import time
import serial
import numpy as np
import pandas as pd
from sklearn import linear_model as lm
import pickle

class TiltThread(threading.Thread, classifier, feature_function):
      """Threaded Url Grab"""
  def __init__(self, queue, out_queue,  classifier, feature_function):
      threading.Thread.__init__(self)
      self.out_queue = out_queue
      self.classifier = classifier
      self.feature_function = feature_function

  def feature_extract(self, segment):
      #extract features
      array = np.array(segment).astype(float)
      m = np.mean(array, 0)    # returns an array of means
      v = np.var(array, 0)     # returns an array of variances
      features = np.append(m,v)    # creates a [1 X 12] array
    return features

    def run(self):
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
          predict = self.classifier.predict(self.feature_function(sample))
          if predict.item(0) == 1:      # 'predict' is a numpy ndarray object
            windowList = []
          else:
            del windowList[:(window / 2)]         # overlap readings by 50%
            tookpill = predict.item(0)
            self.out_queue.put(tookpill)
            self.out_queue.task_done()


class ThreadUC(queue, out_queue):
    """Threaded patient caretaker quque"""
    def __init__( queue, uc_queue):
        threading.Thread.__init__(self)
        self.uc_queue = uc_queue
        self.queue = queue

    def run(self):
      while True:
        ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
        comm_val = int(ser.readline())
        self.uc_queue.put( comm_val )
        self.queue.task_done()



#####main#############
def main():
  clf = pickle.load(open("LG_Classifier.p", "rb"))
  tookpill = 0
  uc_comm  = 0

  #spawn a pool of threads, and pass them queue instance
  for i in range(5):
        t = TiltThread(in_queue,uc_queue)
        t.setDaemon(True)
        t.start()
        tookpill = t.get()
    in_queue.join()
    uc_queue.join()
    print '****pil info****'
    print tookpill
    print "*******"

    for i in range(5):
        dt = ThreadUC(queue, out_queue)
        dt.setDaemon(True)
        dt.start()
        uc_comm = dt.get()
    queue.join()
    out_queue.join()
    print "***user patient****"
    if uc_comm = 1:
      print "****USR MSG****"
    if uc_comm = 2:
      print "****CARETAKER"
      print caretaker


for i in range(10000):
main()





