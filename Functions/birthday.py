#Birthday function
#Purpose: Able to store the user's birthday and when it matches the current date wish them ahppy birthday
#Version: Python 3.9
#04-30-2021
#Shravya Bingi
#Dependencies: datetime module, main.py

import datetime

def birthday():
    try:
        with open ('birthday.txt', "r") as f:
            date = f.read()
            user_month = date[0:2]
            #user_month = int(user_month)
            user_date = date[2:5]
            #user_date = int(user_date)
            user_birth = "{}/{}".format(user_month, user_date)
            return user_birth
    except:
        with open('birthday.txt', "x") as g:
            user_month = input("Enter the month of your birthday in two digits: ")
            user_date = input("Enter the date of your birthday in two digits: ")
        with open('birthday.txt', "w") as g:
            g.write(user_month)
            g.write(user_date)
            print("Birthday has been stored")


def birthday_wish():
    try:
        wish = birthday()
        if date_now == wish:
            output = "Happy Birthday!"
            return output
        else:
            print(" ")
    except:
        print(" ")




date = datetime.datetime.now()
date_now = (date.strftime("%m/%d"))


print(birthday_wish())
