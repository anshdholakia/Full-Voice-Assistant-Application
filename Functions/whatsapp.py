# Name: whatsapp.py
# Purpose: Opens whatsapp web for the user
# Version: Python 3.8.3
# 7-05-2021
# Ansh Dholakia
# Dependencies: webbrowser module


import webbrowser

try:
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(f'https://web.whatsapp.com/')

except Exception as e:
    webbrowser.open(f'https://web.whatsapp.com/')
