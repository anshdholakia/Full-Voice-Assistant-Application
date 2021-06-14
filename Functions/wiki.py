import webbrowser 

c = input (" What would you like to search for in wikipedia : ")
b = "https://en.wikipedia.org/wiki/" 
d =  b + c
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open_new('https://en.wikipedia.org/wiki/'+ c)
