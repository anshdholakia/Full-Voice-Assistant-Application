# Name: voice_typing.py
# Purpose: Prints speech of the user in a textbox
# Version: Python 3.8.3
# 11-03-2021
# Ansh Dholakia
# Dependencies: speech_recognition and pyautogui module

import speech_recognition as sr
import pyautogui
def takeCommand():
        '''
        It takes microphone input form user and string as output
        '''

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.phrase_threshold = 0.0
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio,language='en-UK')
            return query

        except Exception as e:
            # print(e)
            return "None"


query = takeCommand()
while ("quit" not in query):
    if (query == "None" or query == None or query == "none"):
        pass
    else:
        pyautogui.write(f" {query} ", interval=0.01)

    query = takeCommand()


