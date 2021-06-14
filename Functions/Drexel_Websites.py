#Drexel Websites Function
#Purpose: Opens the proper Drexel website when prompted to 
#Version: Python 3.9
#05-20-2021
#Shravya Bingi
#Dependencies: webbrower module, main.py

import webbrower

def Drexel_One():
    try:
        webbrower.open("https://one.drexel.edu/web/university/welcome")
    except:
        print("Unable to open the website at this time")


def BBLearn():
    try:
        webbrowser.open("https://learn.dcollege.net/ultra/institution-page")
    except:
        print("Unable to open the website at this time")

def drexel_website():
    try:
        webbrowser.open("https://drexel.edu")
    except:
        print("Unable to open the website at this time")

#call proper functions
Drexel_One()
BBLearn()
drexel_website()
