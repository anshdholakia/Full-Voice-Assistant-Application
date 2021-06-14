# Name: news_alert.py
# Purpose: gets and prints out the top 7 headlines from the google news
# Version: Python 3.9.5
# 05-03-2021
# Saquib Baig
# Dependencies: 'bs4' module, 'urllib.request' module, 'win32com.client' module, 'sys' module



import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from win32com.client import Dispatch
import sys

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()
x = 0

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
     print(news.title.text)
     s = news.title.text
     speak = Dispatch("SAPI.Spvoice")
     speak.Speak(s)  
     x = x + 1
     if x == 7: 
        sys.exit() 
 
    
