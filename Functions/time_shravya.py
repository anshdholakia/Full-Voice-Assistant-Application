#Time Function
#Purpose: Returns the current time when prompted to
#Version: Python 3.9
#02-28-2021
#Shravya Bingi
#Dependencies: datetime, pytz modules, main.py


#Get the modules from python
'''
This part of the code was acquired from "https://www.pythonprogramming.in/get-current-time-in-mst-est-utc-and-gmt.html"
'''
from datetime import datetime
import pytz
tz = pytz.timezone('America/New_York')
time_1 = datetime.now(tz)
''' The part of the code that was acquired ends here'''
time = time_1.strftime("%I:%M")
print("The current time is:", time)
