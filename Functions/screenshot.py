#Screenshot Function
#Purpose: Allows the user to take a screenshot of their page
#Version: Python 3.9
#02-17-2021
#Shravya Bingi
#Dependencies: pyautogui, cv2, tkinter, numpy, and sys modules , main.py

import pyautogui #This module is in charge of controlling mouse and keyboard
import cv2
import tkinter as tk
import numpy as np
import sys
window = tk.Tk()

#take is the function for screenshot
def take():
    image = pyautogui.screenshot() 
    screenshot = image
    screenshot.save(f'{sys.path[0]}/Oliver_Screenshot.png')

take() #calling the function so it runs
