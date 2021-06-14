# Name: play_songs.py
# Purpose: Directs the user to the youtube music with the specified song
# Version: Python 3.8.3
# 04-05-2021
# Ansh Dholakia
# Dependencies: webbrowser module

import webbrowser

song = input("Enter song name: ")
try:
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(f'https://music.youtube.com/search?q={song}')

except Exception as e:
    webbrowser.open(f'https://music.youtube.com/search?q={song}')
