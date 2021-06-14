# Name: amazon.py
# Purpose: it takes the name of the product the user wants to search for and opens the relevant product search page in amazon
# Version: Python 3.9.5
# 29-04-2021
# Saquib Baig
# Dependencies: webbrowser module



import webbrowser 

search_word = input(("What product would you like to search for in amazon? "))

webbrowser.open('https://www.amazon.in/s?k='+search_word+'&ref=nb_sb_noss') 






