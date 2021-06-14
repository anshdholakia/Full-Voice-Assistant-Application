# Name: python_doc_function.py
# Purpose: Open Python website
# Version: Python 3.8.3
# 25-05-2021
# Ansh Dholakia
# Dependencies: webbrowser module
import webbrowser

try:
    webbrowser.open("https://www.python.org/")

except:
    print("Sorry, cannot open python documentation for you")
