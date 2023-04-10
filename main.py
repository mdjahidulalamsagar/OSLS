import os
import datetime
# from datetime import datetime

# declare variables
fileName = 'demo.txt'
lastModifiedTime = 0
wakeUpTime = 0

# call this just first time
# now = datetime.date.now()
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("Wake up time",dt_string)

while True:
      currentTimeStamp = os.stat(fileName).st_mtime
      if currentTimeStamp != lastModifiedTime:
            lastModifiedTime = currentTimeStamp
            print("modified")
