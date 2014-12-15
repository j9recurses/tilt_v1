#!/usr/bin/python
import threading

def update_pill(threadName, delay):
  if counterpill%5:
      pilltaken = 1
      counterpill = counterpill +1
      time.sleep(delay)
      print  threadName
      return pilltaken

def checkpillstatus(threadName, delay):
  if pilltaken:
      print "Awesome the user took their"
      time.sleep(delay)
      print  threadName


pilltaken = myThread(1, "Thread-1", 1, counterpill, pilltaken)
thread2 = myThread2(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"
