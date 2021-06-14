# Name: google_drive.py
# Purpose: opens the google drive
# Version: Python 3.9.5
# 21-05-2021
# Saquib Baig
# Dependencies: webbrowser module


import webbrowser 

try: 
    webbrowser.open('https://drive.google.com/drive/u/0/my-drive') 
except:
    print("There was an error opening the google drive at this time.")
