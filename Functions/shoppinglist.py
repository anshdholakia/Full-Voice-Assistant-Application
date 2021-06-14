# Name: shoppinglist.py
# Purpose: takes inputs from the user and creates a shopping list in a .txt file with the inputs from the user
# Version: Python 3.9.5
# 28-04-2021
# Saquib Baig
# Dependencies: 'speech_recognition' module


import speech_recognition as sr


print("\nPlease speak \"The end of the list\" to exit")
Shoppinglist = []
q = ""
print

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.phrase_threshold = 0.0
        audio = r.listen(source)

    try:  
        query = r.recognize_google(audio,language='en-IN')
        q = str(r.recognize_google(audio,language='en-IN'))
        print(f"Your response: {query}\n")

    except Exception as e:
        # print(e)
        # speak("Sorry, I was not able to understand you")
        print("Sorry, I was not able to understand you")
        return "None"

    return query


i =  0
while q != 'the end of the list':
    q = takeCommand()
    Shoppinglist.append(q)
    i+=1
    z = str(i)
    file1 = open("Shoppinglist.txt", "a")  # append mode
    if q != 'none' and q != 'the end ofthe list':
        file1.write("%s) " %(z))
        file1.write(q+"\n")
    file1.close()

print(Shoppinglist)
