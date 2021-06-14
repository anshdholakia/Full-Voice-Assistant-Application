import webbrowser 
year = int(input("Enter the year(4 digits):"))
month = int(input("Enter the month(2 digits):"))
day = int(input("Enter the date(2 digits)"))
user_date = ('https://calendar.google.com/calendar/u/0/r/day/' + str(year) + "/" + str(month) + "/" + str(day))
webbrowser.open(user_date)
