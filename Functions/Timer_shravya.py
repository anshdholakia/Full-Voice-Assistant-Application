#Timer Function
#Purpose: Allows the user to pick a specific time and then counts down 
#Version: Python 3.9
#04-09-2021
#Shravya Bingi
#Dependencies: time, threading, sys modules, main.py


import time
from threading import Timer
import sys

def timeout(timee):

    while timee:
        mins, secs = divmod(timee, 60)

        timer = '{:02d}:{:02d}'.format(mins, secs)

        print(timer, end="\r")

        time.sleep(1)

        timee -= 1

    print("Time is up!")
    sys.exit()
    

timeee = input("Enter the time in seconds: ")

t = Timer(int(timeee), timeout(int(timeee)))
t.start()





