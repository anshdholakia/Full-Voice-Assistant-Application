#Resume function
#Purpose: Able to go into another team's resume builder website (we asked for permission and they gladly allowed us to "collab" with them)
#Version: Python 3.9
#05-26-2021
#Shravya Bingi
#Dependencies: webbrowser module, main.py
#We collaborated with 67WebPANS and their resume builder is Resumify


import webbrowser
try:
    webbrowser.open(home-page.resumebuilder.repl.co)
except:
    print("This website cannot be opened at this time")
