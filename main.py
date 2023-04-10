import os
import time
from datetime import datetime

# declare variables
fileName = 'demo.txt'
lastModifiedTime = 0
wakeUpTime = 0

# date time format for date time object
def readableDateFormat(givenTime):
      return givenTime.strftime("%d/%m/%Y %H:%M:%S")

# date time format for st_mtime
def st_mtime_to_readable_DateFormat(st_mtime_time):
      return readableDateFormat(datetime.fromtimestamp(st_mtime_time))

# call this function first time
def wakeUp():
      now = datetime.now()
      print("Wakeup:", readableDateFormat(now))

# print last line of file
def readLastLine():
      logFile = open(fileName, 'r')
      try:
            *_ , last_line = logFile.readlines()
            print(last_line)
      except:
            print("file is empty")
      
      logFile.close()

# file watcher function
def FileWatcher(lastModifiedTime):
      while True:
            currentTimeStamp = os.stat(fileName).st_mtime
            if currentTimeStamp != lastModifiedTime:
                  lastModifiedTime = currentTimeStamp 
                  print("modified at",st_mtime_to_readable_DateFormat(lastModifiedTime))
                  readLastLine()
            time.sleep(0.2)
                  
                  

wakeUp()
FileWatcher(lastModifiedTime)
