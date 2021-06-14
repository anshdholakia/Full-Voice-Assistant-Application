# Name: Battery_alert.py
# Purpose: pops a small window showing the battery percentage of the user's laptop every 1 hour
# Version: Python 3.9.5
# 17-02-2021
# Saquib Baig
# Dependencies: psutil module and time module


import psutil 
# from plyer import notification 
import time 
  
  
battery = psutil.sensors_battery() 
  
# from psutil we will import the  
# sensors_battery class and with 
# that we have the battery remaining 
while(True): 
    percent = battery.percent 
    print(percent)
      
    # after every 60 mins it will show the 
    # battery percentage 
    time.sleep(60*60) 
      
    continue
