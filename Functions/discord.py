#Discord Function
#Purpose: Able to open Discord when run in a new tab
#05-07-2021
#Shravya Bingi
#Dependencies: webbrowser module, main.py

import webbrowser

try:
    webbrowser.open('https://discord.com/channels/@me')
except:
    print("Unable to access Discord at this time")
