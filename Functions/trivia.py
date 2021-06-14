# Name: trivia.py
# Purpose: Asks true/false and mcqs and gives correct answers.
# Version: Python 3.8.3
# 09-04-2021
# Ansh Dholakia
# Dependencies: requests, json, random module

import json
import random
import requests

print("Welcome to the trivia game!")

r = requests.get("https://opentdb.com/api.php?amount=100")
data = eval(r.text)

questions = data['results']
answer = "e"
i = 0

answers = {"a" : 0, "b" : 1, "c" : 2, "d" : 3}

while(answer != "exit"):

    i = random.randint(0, 50)
    questions[i]['question'] = questions[i]['question'].replace("&quot;", "")
    if (questions[i]['type'] == "boolean"):
        print("\nTrue or False?")
        print(f"{questions[i]['question']}")
        answer = input("Enter your answer: ")
        if (answer.lower() == questions[i]['correct_answer'].lower()):
            print("Correct Answer!")
        else:
            print("Incorrect Answer!")
    
    else:
        print(f"\n{questions[i]['question']}")
        correct_answer = questions[i]['correct_answer']
        lis = [f"{questions[i]['correct_answer']}", f"{questions[i]['incorrect_answers'][0]}", f"{questions[i]['incorrect_answers'][1]}", f"{questions[i]['incorrect_answers'][2]}"]
        random.shuffle(lis)
        option = ["A - ", "B - ", "C - ", "D - "]
        ind = lis.index(correct_answer)
        indss = 0
        for item in lis:
            print(option[indss] + item)
            indss += 1

        answer = input("Enter your input: ")

        try:
            if (answers[answer] == ind):
                print("Correct!")
            else:
                print(f"Incorrect, the correct answer was {lis[ind]}")

        except Exception as e:
            print("Wrong input! Next question")
            