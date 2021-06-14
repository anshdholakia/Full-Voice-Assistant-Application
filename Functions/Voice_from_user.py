# Name: Voice_from_user.py
# Purpose: Takes the voice from user and prints it
# Version: Python 3.8.3
# 19-02-2021
# Ansh Dholakia
# Dependencies: speech_recognition module, recognize_google class

import speech_recognition as sr


def takeCommand():
    '''
    It takes microphone input form user and string as output
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.phrase_threshold = 0.0
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-UK')
        print(f"Your response: {query}\n")

    except Exception as e:
        # print(e)
        # speak("Sorry, I was not able to understand you")
        print("Sorry, I was not able to understand you")
        return "None"

    return query

takeCommand()


