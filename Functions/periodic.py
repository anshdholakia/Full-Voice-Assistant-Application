# Name: periodic.py
# Purpose: Prints periodic name corresponsing to the atomic number
# Version: Python 3.8.3
# 25-04-2021
# Ansh Dholakia
# Dependencies: requests module

import requests

print("Opening Periodic Table")
try:
    num = int(input("Enter atomic number: "))
    r = requests.get(f"https://neelpatel05.pythonanywhere.com/element/atomicnumber?atomicnumber={num}")
    data = eval(r.text)
    print(data['name'])


except Exception as e:
    print("Error")
