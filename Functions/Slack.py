#Slack function
#Purpose: Able to open the slack website when run in a new tab
#Version: Python 3.9
#04-23-2021
#Shravya Bingi
#Dependencies: webbrowser module, main.py



#import proper modules
import webbrowser

#try to open Slack
try:
    webbrowser.open('https://slack.com')
except: #Runs except when needed
    print("Unable to access Slack at this time")
