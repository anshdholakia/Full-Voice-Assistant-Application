# Name: stock_market.py
# Purpose: Opens yahoo finance for the user
# Version: Python 3.8.3
# 21-05-2021
# Ansh Dholakia
# Dependencies: webbrowser module

import webbrowser

try:
    webbrowser.open('https://finance.yahoo.com/')

except Exception as error:
    print("Sorry, cannot open stock market")