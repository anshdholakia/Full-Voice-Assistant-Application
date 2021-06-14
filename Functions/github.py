# Name: github.py
# Purpose: opens the github website
# Version: Python 3.9.5
# 21-05-2021
# Saquib Baig
# Dependencies: webbrowser module


import webbrowser

try: 
    webbrowser.open('https://github.com/')
except:
    print("There was an error when opening the github")
