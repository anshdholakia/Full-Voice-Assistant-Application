# Name: google_maps.py
# Purpose: opens the location user wants in the google maps
# Version: Python 3.9.5
# 26-02-2021
# Saquib Baig
# Dependencies: webbrowser module


import webbrowser 

map_string = input("What location would like to search for? : ")
webbrowser.open('https://www.google.com/maps/place/' + map_string) 
