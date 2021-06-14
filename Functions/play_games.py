# Name: play_games.py
# Purpose: Plays Magic-8 Ball with the User
# Version: Python 3.8.3
# 12-03-2021
# Ansh Dholakia
# Dependencies: speech_recognition module

import speech_recognition as sr
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

answer_list = ["Probably", "Yes", "I don't think so", "Plausible", "Improbable", "Never", "Definitely"]

query = takeCommand()
while ("quit" not in query):
    if (query == "None" or query == None or query == "none"):
        pass
    else:
        import random
        print(random.choice(answer_list))

    query = takeCommand()


