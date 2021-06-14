#Open Google Function
#Purpose: Prompts the user to enter what they want to search for and then opens up a google tab with the searched item
#Version: Python 3.9
#03-05-2021
#Shravya Bingi
#Dependencies: webbrower module, main.py


import webbrowser

search_string = input("What would you like to seacrh for?:")
url = "https://www.google.com.tr/search?q={}".format(search_string)
webbrowser.open_new_tab(url)
