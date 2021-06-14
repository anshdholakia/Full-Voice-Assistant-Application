#Tiktok Function
#Purpose: Able to open tiktok when run in a new tab
# 05-13-2021
#Shravya Bingi
#Dependencies: Webbrowser module, main.py

import webbrowser

try:
    webbrowser.open('https://www.tiktok.com/?is_copy_url=1&is_from_webapp=v1')
except:
    print("Website cannot be opened at this time")
