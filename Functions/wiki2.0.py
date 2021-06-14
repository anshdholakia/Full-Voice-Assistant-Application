# Name: wiki2.0.py
# Purpose: Asks the user for which information to search for in wikipedia and then extracts and prints the extracted information from the relevant wikipedia page.
# Version: Python 3.9.5
# 24-02-2021
# Saquib Baig
# Dependencies: wikipedia module


import wikipedia

answer = input(" What would you like to search for in wikipedia? :")
result = wikipedia.summary(answer , sentences = 2)
print(result)
