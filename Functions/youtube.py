# Name: youtube.py
# Purpose: It takes what the user wants to search for in youtube as input and then opens the relevant youtube search page
# Version: Python 3.9.5
# 05-03-2021
# Saquib Baig
# Dependencies: webbrowser module



import webbrowser 

map_string = input("What would you like to search for in youtube? : ")
webbrowser.open('https://www.youtube.com/results?search_query=' + map_string) 
