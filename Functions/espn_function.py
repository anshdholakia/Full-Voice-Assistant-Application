# Name: espn_function.py
# Purpose: Open ESPN website
# Version: Python 3.8.3
# 13-05-2021
# Ansh Dholakia
# Dependencies: webbrowser module
import webbrowser

try:
    webbrowser.open("https://www.espn.com/")

except:
    print("Sorry, cannot open espn for you")