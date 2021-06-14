# Name: units_conversion.py
# Purpose: Converts lenght, temperature, currency, weight, and volume units
# Version: Python 3.9.5
# 12-03-2021
# Saquib Baig
# Dependencies: platform module, 'CurrencyConverter' package from the 'currency_converter' module


import platform
from currency_converter import CurrencyConverter

quantity = input ('What quantity do you want to convert: ')
unit1 = input('Which unit do you want it converted from:  ')
unit2 = input('Which unit do you want it converted to: ')
num1 = input('Enter the value: ')

if quantity == "length":

    if unit1 == "cm" and unit2 == "m":
      ans = float(num1)/100
      print(ans, "\n")
    elif unit1 == "mm" and unit2 == "cm":
      ans = float(num1)/10
      print(ans, "\n")
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1)*100
        print(ans, "\n")
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1)*10
        print(ans, "\n")
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1)/1000
        print(ans, "\n")
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1)*1000
        print(ans, "\n")
    elif unit1 == "km" and unit2 == "m":
        ans = float(num1)*1000
        print(ans, "\n")
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1)/1000
        print(ans, "\n")
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1)/1000000
        print(ans, "\n")
    elif unit1 == "ft" and unit2 == "cm":
        ans = float(num1)*30.48
        print(ans, "\n")
    elif unit1 == "ft" and unit2 == "mm":
        ans = float(num1)*304.8
        print(ans, "\n")
    elif unit1 == "ft" and unit2 == "inch":
        ans = float(num1)*12
        print(ans, "\n")
    elif unit1 == "inch" and unit2 == "cm":
        ans = float(num1)*2.54
        print(ans, "\n")
    elif unit1 == "inch" and unit2 == "mm":
        ans = float(num1)*25.4
        print(ans, "\n")


if quantity == "temperature":

    if unit1 == "c" and unit2 == "f" :
        farhenheit = (float(num1) * 1.8) + 32
        print(farhenheit, "farhenheit\n")

    elif unit1 == "c" and unit2 == "k" :
        kelvin = float(num1) + 273.15
        print(kelvin, "kelvin\n")

    elif unit1 == "f" and unit2 == "c" :
        celcius = (float(num1)-32)*1.8
        print(celcius, "celcius\n")

    elif unit1 == "f" and unit2 == "k" :            
        kelvin = (num1-32)*1.8 + 273.15
        print(kelvin, "kelvin\n")

    elif unit1 == "k" and unit2 == "c" :            
        celcius = num1 - 273.15
        print(celcius, "celcius\n")
    
    elif unit1 == "k" and unit2 == "f" :  
        farhenheit =  ((float(num1) - 273.15)  * 1.8) + 32      
        print(farhenheit, "farhenheit\n",) 
        
if quantity == "currency":

    c = CurrencyConverter()
    
    if unit1 == "eur" and unit2 == "usd":
          print(c.convert(num1, 'EUR', 'USD'), "\n")
    if unit1 == "usd" and unit2 == "eur":
          print(c.convert(num1, 'USD', 'EUR'), "\n")
    if unit1 == "inr" and unit2 == "usd": 
          print(c.convert(num1, 'INR', 'USD'), "\n")
    if unit1 == "usd" and unit2 == "inr": 
         print(c.convert(num1, 'USD', 'INR'), "\n")
    if unit1 == "inr" and unit2 == "eur":
         print(c.convert(num1, 'INR', 'EUR'), "\n")
    if unit1 == "eur" and unit2 == "inr":
         print(c.convert(num1, 'EUR', 'INR'), "\n")


if quantity == "weight":
    if unit1 == "kg" and unit2 == "lb":
        pound = 2.20462
        converted_weight = float(weight * pound)
        formatted_float = "{:.2f}".format(converted_weight)
        print(formatted_float, "\n")

    if unit1 == "lb" and unit2 == "kg":
        pound = 2.20462
        converted_weight = float(weight / pound)
        formatted_float = "{:.2f}".format(converted_weight)
        print(formatted_float, "\n")


if quantity == "volume":

    if unit1 == "litre" and unit2 == "ml":
        conversion = num1 * 1000
        print(conversion, "\n")

    if unit1 == "ml" and unit2 == "litre":
        conversion = num1 / 1000
        print(conversion, "\n")

    if unit1 == "gallons" and unit2 == "litre":
        conversion = num1 * 3.785
        print(conversion, "\n")

    if unit1 == "litre" and unit2 == "gallons":
        conversion = num1 / 3.785
        print(conversion, "\n")        

