# Name: audible.py
# Purpose: opens the user's book in the audible search page
# Version: Python 3.9.5
# 28-05-2021
# Saquib Baig
# Dependencies: webbrowser module


import webbrowser

search_word = input("Which book would you like to open in Audible: ")

try: 
    webbrowser.open('https://www.audible.in/search?keywords='+search_word+'&ref=a_ep_podcas_t1_header_search')
except:
    print("There was an error when opening the book")
