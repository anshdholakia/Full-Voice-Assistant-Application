# Name: files.py
# Purpose: It  takes the name and type of the file to create as input from the user and creates a new file.
# Version: Python 3.9.5
# 15-04-2021
# Saquib Baig
# Dependencies: no module is required



file_type = input("What file type would you like to create - word or txt: ")
filename = input("What would you like to name the file: ")

f = filename + '.' + file_type

f= open(f, "w+")
