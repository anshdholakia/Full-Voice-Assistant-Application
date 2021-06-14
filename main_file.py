# Name: main_file.py
# Purpose: Code for the Main Application including the GUI, and different functionalities.
# Version: Python 3.8.3
# 16-05-2021
# Ansh Dholakia, Shravya Bingi, Saquib Baig, Vani Patel
# Dependencies: tkinter, Pillow, speech_recognition, time, psutil, webbrowser, winapps, datetime, sys, requests, json, math, pytz, os, threading, subprocess modules.


# import these modules
from tkinter import *
import tkinter.scrolledtext as stt
import tkinter.messagebox as tsmg
from tkinter import colorchooser
from PIL import ImageTk, Image
import speech_recognition as sr
import time
import psutil
import webbrowser
import winapps
import datetime
import sys
import requests
import json
import math
import pytz
import os
from threading import Timer
import subprocess as sp


# initializing the height and width of tkinter app
h = 500
w = 600
connect = 0


# main GUI class for root
class GUI(Tk):
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        # making a frame
        self.container = Frame(self)

        self.container.pack(side="top", fill="both", expand=True)


        # using grid to stretch it and cover the whole screen
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen
        self.x = (ws/2) - (w/2)
        self.y = (hs/2) - (h/2)-20
        self.geometry('%dx%d+%d+%d' % (w, h, self.x, self.y))
        self.minsize(w, h)
        # self.maxsize(w, h)

        # Putting title on the window
        self.title("Oliver | Voice Assistant")
        self.wm_iconbitmap("logo.ico")
        self.var = StringVar()

        # Setting the status bar
        self.var.set(f"Oliver | Disabled")
        self.statusbar = Label(
            self.container, textvar=self.var, relief=RIDGE, anchor=W, background="snow")
        self.statusbar.grid(row=2, column=0, sticky='nsew')

        self.frames = {}
        self.status_deactive()


    # Changing the status bar information and going to ChatPage
    def status_active(self):
        global connect
        connect = 1

        frame = ChatPage(self.container, self)
        self.frames[ChatPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ChatPage)

        # Changin the status bar
        self.var.set(f"Oliver | Active | Click on the input button")

    # Changing status bar to deactivated and Going to Seetings Page
    def settingboi(self):
        frame = SettingsPage(self.container, self)
        self.frames[SettingsPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(SettingsPage)
        self.var.set(f"Oliver | Disabled | Settings")


    # Changing status bar to deactivated and Going to Welcome Page
    def status_deactive(self):
        global connect
        connect = 0

        frame = StartPage(self.container, self)

        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        self.var.set(f"Oliver | Disabled")

    # Raising frame on the window
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



# Welcome window
class StartPage(Frame):
    def __init__(self, parent, controller):
        global set_f
        set_f.seek(0)

        Frame.__init__(self, parent, background=f'{set_f.readlines()[1].strip()}')
        set_f.seek(0)

        frame2 = Frame(self, borderwidth=0,
                       background=f'{set_f.readlines()[1].strip()}')
        set_f.seek(0)

        frame2.pack(fill="both", expand=True, padx=20, pady=60)

        image = Image.open('inside_logo.ico')

        image = image.resize((103, 123), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(image)
        # Sets the image too the label
        logo = Label(frame2, image=photo, borderwidth=0)
        # Make the image actually display (If I don't include this it won't display an image)
        logo.photo = photo
        logo.pack(pady=(10, 5))

        Label(frame2, text=f"Hello, it's Oliver!", font="Calibri 37",
              background=f"{set_f.readlines()[1].strip()}", foreground="Black").pack(pady=(0, 5))

        set_f.seek(0)

        Label(frame2, text=f"Your personal voice assistant", font="Calibri 20",
              background=f"{set_f.readlines()[1].strip()}", foreground="Black").pack()

        set_f.seek(0)

        Button(frame2, text="Activate", command=lambda: controller.status_active(), relief=RIDGE,
               font="Calibri 20", background='gray99', foreground="black").pack(ipadx=10, ipady=0, padx=30, pady=30)

# This is the chatting page
class ChatPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background="alice blue")

        menu = Frame(self, borderwidth=0, background='snow')
        menu.pack(fill="both", side=TOP)

        # Putting Buttongs for Home and Settings
        button1 = Button(menu, text="Home",
                         command=lambda: controller.status_deactive(), relief=RIDGE, font="Calibri 12", background="alice blue")
        button1.pack(side=LEFT, pady=(7, 4), padx=(10, 0), ipadx=5, ipady=0)

        sett_but = Button(menu, text="Settings", command=lambda: controller.settingboi(),
                          relief=RIDGE, bg="alice blue", font="Calibri 12")
        sett_but.pack(side=LEFT, pady=(7, 4), padx=(10, 0), ipadx=5, ipady=0)

        image = Image.open('logo.ico')
        image = image.resize((27, 33), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        # Sets the image too the label
        logo = Label(menu, image=photo, borderwidth=0)

        # Make the image actually display (If I don't include this it won't display an image)
        logo.photo = photo

        logo.pack(pady=(10, 5), side=RIGHT, padx=(0, 10))

        label = Label(menu, text="Oliver",
                      font="Calibri 22", background="snow")
        label.pack(pady=(10, 7), padx=0, side=RIGHT)

        self.frame2 = Frame(self, borderwidth=0, background='snow2')
        self.frame2.pack(fill="both", expand=True, padx=10, pady=0)

        TextBox = stt.ScrolledText(
            self.frame2, wrap=WORD, bg="alice blue", height=10, font=("Calibri", 12 if set_f.read(1) == "1" else 18))
        Start_assistant(TextBox, self.frame2)


# TODO: Setting Page
class SettingsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background="alice blue")

        menu = Frame(self, borderwidth=0, background='snow')
        menu.pack(fill="both", side=TOP)

        # Making back buttons
        button4 = Button(menu, text="Back",
                         command=lambda: controller.status_active(), relief=RIDGE, font="Calibri 12", background="alice blue")
        button4.pack(side=LEFT, pady=(7, 4), padx=(10, 0), ipadx=5, ipady=0)

        image = Image.open('logo.ico')
        image = image.resize((27, 33), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        # Sets the image too the label
        logo = Label(menu, image=photo, borderwidth=0)

        # Make the image actually display (If I don't include this it won't display an image)
        logo.photo = photo

        logo.pack(pady=(10, 5), side=RIGHT, padx=(0, 10))

        # Creating the branding of Oliver on Settings Page
        label = Label(menu, text="Oliver",
                      font="Calibri 22", background="snow")
        label.pack(pady=(10, 7), padx=0, side=RIGHT)

        self.frame3 = Frame(self, borderwidth=0, background='snow2')
        self.frame3.pack(fill="both", expand=True, padx=10, pady=0)

        horizontal_frame = Frame(self.frame3, background="snow2")

        label1 = Label(horizontal_frame, text="Font size", bg="snow2",
                       font="Calibri 15", fg="black", padx=10, pady=10)

        label1.grid(row=0, column=0)

        # Using the set_f pointer to read the contents of file
        global set_f

        # Used for logging the clicks
        v = StringVar(self.frame3, f"{set_f.read(0)}")

        # Seeking at the 0th character so it reads from the beginning
        set_f.seek(0)

        small_button = Radiobutton(horizontal_frame, text="Small Text", font="Calibri 13", variable=v,
                                   value=1, indicator=0, background=f"{set_f.readlines()[1].strip()}", command=lambda: self.Change(1))
        set_f.seek(0)

        small_button.grid(row=0, column=1, ipady=4.5,
                          padx=(0, 20), sticky="nsew")

        big_button = Radiobutton(horizontal_frame, text="Big Text", font="Calibri 18", variable=v,
                                 value=2, indicator=0,
                                 background=f"{set_f.readlines()[1].strip()}", command=lambda: self.Change(2))

        set_f.seek(0)

        big_button.grid(row=0, column=2, sticky="nsew")

        # Configuring the horizontal frame so it shows on the screen
        horizontal_frame.grid_columnconfigure(0, weight=1)
        horizontal_frame.grid_columnconfigure(1, weight=1)
        horizontal_frame.grid_columnconfigure(2, weight=1)
        horizontal_frame.grid_columnconfigure(3, weight=1)

        horizontal_frame.pack(fill="x", expand=True, padx=10, pady=0)

        horizontal_frame2 = Frame(self.frame3, background="snow2")

        label12 = Label(horizontal_frame2, text="Oliver Voice",
                        bg="snow2", font="Calibri 15", fg="black", padx=10, pady=10)

        label12.grid(row=0, column=0)

        v2 = StringVar(self.frame3, f"{set_f.read(0)}")

        # Makign the Yes button
        yes_button = Radiobutton(horizontal_frame2, text="On", font="Calibri 15", variable=v2,
                                 value=1, indicator=0, background="OliveDrab1", command=lambda: self.Change(3))

        yes_button.grid(row=0, column=1, padx=(0, 20), sticky="nsew")


        # Makign the No Button
        no_button = Radiobutton(horizontal_frame2, text="Off", font="Calibri 15", variable=v2,
                                value=2, indicator=0,
                                background="salmon1", command=lambda: self.Change(4))

        no_button.grid(row=0, column=2, sticky="nsew")

        horizontal_frame2.grid_columnconfigure(0, weight=1)
        horizontal_frame2.grid_columnconfigure(1, weight=1)
        horizontal_frame2.grid_columnconfigure(2, weight=1)
        horizontal_frame2.grid_columnconfigure(3, weight=1)

        horizontal_frame2.pack(fill="x", expand=True, padx=10, pady=0)

        horizontal_frame3 = Frame(self.frame3, background="snow2")

        label13 = Button(horizontal_frame3, text="Theme Color",
                         bg=f"{set_f.readlines()[1].strip()}", font="Calibri 15", fg="black", padx=10, pady=10, command=lambda: self.Change(5))

        label13.grid(row=0, column=0)

        horizontal_frame3.grid_columnconfigure(0, weight=1)
        horizontal_frame3.grid_columnconfigure(1, weight=1)
        horizontal_frame3.grid_columnconfigure(2, weight=1)
        horizontal_frame3.grid_columnconfigure(3, weight=1)

        horizontal_frame3.pack(fill="x", expand=True, padx=10, pady=0)

        horizontal_frame4 = Frame(self.frame3, background="snow2")

        # About us button
        label13 = Button(horizontal_frame4, text="Team behind Oliver",
                         bg="snow", font="Calibri 15", fg="black", padx=10, pady=10, command=lambda: self.Change(6))

        label13.grid(row=0, column=0)

        horizontal_frame4.grid_columnconfigure(0, weight=1)
        horizontal_frame4.grid_columnconfigure(1, weight=1)
        horizontal_frame4.grid_columnconfigure(2, weight=1)
        horizontal_frame4.grid_columnconfigure(3, weight=1)

        horizontal_frame4.pack(fill="x", expand=True, padx=10, pady=0)


    # When a button is clicked, it will invoke the Change function that will change the settings.txt file
    def Change(self, *args):
        global set_f
        global engine

        set_f.seek(0)

        listt = set_f.readlines()

        set_f.seek(0)

        with open("settings.txt", "w") as setffff:
            if args[0] == 1:
                setffff.write(f"1Text\n{listt[1]}")

            elif args[0] == 2:
                setffff.write(f"2Text\n{listt[1]}")

            elif args[0] == 3:
                engine.setProperty("rate", 178)
                engine.setProperty("volume", 1)
                setffff.write(f"{listt[0]}{listt[1]}")

            elif args[0] == 4:
                engine.setProperty("rate", 80000)
                engine.setProperty("volume", 0)
                setffff.write(f"{listt[0]}{listt[1]}")

            elif args[0] == 5:
                color_code = colorchooser.askcolor(title="Choose color")
                # if the user clicks on cancel
                if color_code[1] != None:
                    color_code = color_code[1]
                    setffff.write(f"{listt[0]}{color_code}\n")
                else:
                    setffff.write(f"{listt[0]}{listt[1]}")

            elif args[0] == 6:
                setffff.write(f"{listt[0]}{listt[1]}")
                tsmg.showinfo(title = "About Us",message = "Oliver is maintained and developed by Team MusicRec62 - \n\nShravya Bingi\nSaquib Baig\nVani Patel\nAnsh Dholakia")


# This class will actually start the voice assistant
class Start_assistant(ChatPage):

    def __init__(self, Canvasee, Mainframe):

        # Getting hold of the frame widgets using arguments
        self.tb = Canvasee
        self.tb.pack(expand=True, fill=BOTH)

        # Making buttons for opening commands
        self.comm_but = Button(Mainframe, text="Commands", relief=RIDGE,
                               command=self.command_window, bg="snow2", font="Calibri 13")
        self.comm_but.pack(side=RIGHT, padx=(0, 20))


        # Makign input button which will invoke the voice assistant
        self.bt = Button(Mainframe, text="Input", command=lambda: self.now_really_startit(
        ), relief=RIDGE, bg="snow", font="Calibri 13")
        self.bt.pack(side=RIGHT, padx=(0, 150))

        # This is for text box
        self.text_input = StringVar()
        self.nameEntered = Entry(
            Mainframe, width=20, textvariable=self.text_input, font=("Calibri", 15))
        self.nameEntered.pack(side=LEFT, padx=(10, 0))

        # Add text in Entry box
        self.nameEntered.insert(0, 'Type Query')
        self.nameEntered.pack(pady=10)

        # Use bind method so it deletes the content in text box on click
        self.nameEntered.bind("<Button-1>", self.click)

        # Putting count to 0 so when the user clicks on the input button again, it wont greet the user
        self.count = 0

    # Call function when we click on entry box
    def click(self, *args):
        self.nameEntered.delete(0, 'end')


    # This will wish user based on the local time
    def WishMe(self):
        # Code for wishing the user
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.assistant_message("Good Morning")
            self.speak("Good Morning")
        elif hour >= 12 and hour < 18:
            self.assistant_message("Good Afternoon")
            self.speak("Good Afternoon")
        else:
            self.assistant_message("Good Evening")
            self.speak("Good Evening")

        self.assistant_message("Please tell me how may I help you?")
        self.speak("Please tell me how may I help you?")

    # The function that actually starts the voice assistant
    def now_really_startit(self):

        # User won't click input button after he clicked it once
        self.bt["state"] = "disabled"

        if (self.count == 0):
            self.WishMe()
            self.count += 1

        # This takes name from the user if not given
        name = self.takename()

        # If the user has typed his query ->
        if (self.nameEntered.get() != "" and self.nameEntered.get() != "Type Query"):
            self.user_message(self.nameEntered.get())
            query = str(self.nameEntered.get()).lower()

        else:
            query = self.takeCommand().lower()

        # To remove the content in text box
        self.click()

        # IF-ELSE Ladder starts from now

        # If the user greets Oliver
        if 'hey oliver' in query or 'hello oliver' in query or 'hello' == query:
            self.assistant_message("Hi...I am here, how can I help?")
            self.speak("Hi...I am here, how can I help?")


        # If user wants wikipedia
        elif 'wikipedia' in query:
            try:
                import wikipedia
                self.speak("Searching Wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                self.assistant_message(results)
                self.speak("According to Wikipedia")
                self.speak(results)

            except Exception as e:
                self.assistant_message("Error encountered!")
                self.speak("Error encountered!")

        # If user wants a timer
        elif 'timer' in query or 'stop watch' in query:

            def timeout(timee):
                self.assistant_message("Timer Activated")
                self.speak("Timer Activated")

                while timee:
                    mins, secs = divmod(timee, 60)

                    timer = '{:02d}:{:02d}'.format(mins, secs)

                    self.assistant_message(f"{timer}\r")

                    time.sleep(1)

                    timee -= 1

                self.assistant_message("Time is up!")
                self.speak("Time is up!")

            self.assistant_message("For how many seconds?")
            self.speak("For how many seconds?")

            try:
                timeee = int(self.takeCommand())

            except Exception:
                while (1):
                    timeee = self.takeCommand()
                    try:
                        timeee = int(timeee)
                        break

                    except Exception as err:
                        self.assistant_message("Error!")
                        continue

            self.t = Timer(int(timeee), timeout(int(timeee)))
            self.t.start()

        # If user wants location
        elif 'where is this place' in query or 'location' in query or 'google maps' in query:

            self.assistant_message("Can you tell me the location")
            self.speak("Can you tell me the location")
            place = self.takeCommand().lower()
            while(place == "none" or place == None or place == "None"):
                self.assistant_message("Can you tell me the location")
                self.speak("Can you tell me the location")

            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://www.google.com/maps/place/{place}')

            except Exception as e:
                webbrowser.open(f'https://www.google.com/maps/place/{place}')


        # If user wants periodic table
        elif 'periodic' in query or 'chemistry table' in query:
            self.assistant_message("Opening Periodic Table")
            self.speak("Opening Periodic Table")
            self.assistant_message("What's the atomic number?")
            self.speak("What's the atomic number?")
            nummm = self.takeCommand().lower()
            while (not nummm.isnumeric()):
                self.assistant_message("What's the atomic number?")
                nummm = self.takeCommand().lower()

            try:
                r = requests.get(
                    f"https://neelpatel05.pythonanywhere.com/element/atomicnumber?atomicnumber={int(nummm)}")
                data = eval(r.text)
                self.assistant_message(
                    f"The corresponding name of the atomic number is: {data['name']}")
                self.speak(
                    f"The corresponding name of the atomic number is {data['name']}")

            except Exception as err:
                self.assistant_message("An unexpected error occured")
                self.speak("An unexpected error occured")

        # If user wants calculator
        elif 'calculator' in query:
            self.assistant_message(
                "Speak\n'addition' for Addition\n'subtraction' for Subtraction\n'multiplication' for Multiplication\n'division' for Division. To quit speak 'exit'")
            self.speak("Speak 'addition' for Addition, 'subtraction' for Subtraction,'multiplication' for Multiplication, 'division' for Division. To quit speak 'exit'")
            command = self.takeCommand().lower()

            while command != "addition" and command != "subtraction" and command != "multiplication" and command != "division" and command != 'exit':
                self.assistant_message("Speak a bit more clearly")
                command = self.takeCommand().lower()

            if command == 'exit':
                self.assistant_message("Closing calculator")
                self.speak("Closing calculator")

            else:
                self.assistant_message("What's your first number?")
                self.speak("What's your first number?")
                first_num = self.takeCommand().lower()
                while (not first_num.isnumeric()):
                    self.assistant_message("What's your first number?")
                    first_num = self.takeCommand().lower()

                self.assistant_message("What's your second number?")
                self.speak("What's your second number?")
                second_num = self.takeCommand().lower()
                while (not second_num.isnumeric()):
                    self.assistant_message("What's your second number?")
                    second_num = self.takeCommand().lower()

                if (command == "addition"):
                    self.assistant_message(
                        f"{first_num} + {second_num} = {int(first_num) + int(second_num)}")
                    self.speak(
                        f"The result is {int(first_num) + int(second_num)}")

                if (command == "subtraction"):
                    self.assistant_message(
                        f"{first_num} - {second_num} = {int(first_num) - int(second_num)}")
                    self.speak(
                        f"The result is {int(first_num) - int(second_num)}")

                if (command == "multiplication"):
                    self.assistant_message(
                        f"{first_num} * {second_num} = {int(first_num) * int(second_num)}")
                    self.speak(
                        f"The result is {int(first_num) * int(second_num)}")

                elif (command == "division"):
                    self.assistant_message(
                        f"{first_num} / {second_num} = {int(first_num) / int(second_num)}")
                    self.speak(
                        f"The result is {int(first_num) / int(second_num)}")


        # If user wants to open notepad
        elif 'notes' in query:
            sp.Popen(['Notepad.exe', 'new_file.txt'])

        # If user wants to open espn
        elif 'espn' in query or 'sports' in query:
            try:
                webbrowser.open("https://www.espn.com/")

            except:
                print("Sorry, cannot open espn for you")


        # If user wants to book tickets
        elif 'book tickets' in query:
            us_state_abbrev = {
                'alabama': 'AL',
                'alaska': 'AK',
                'american samoa': 'AS',
                'arizona': 'AZ',
                'arkansas': 'AR',
                'california': 'CA',
                'colorado': 'CO',
                'connecticut': 'CT',
                'delaware': 'DE',
                'district of columbia': 'DC',
                'florida': 'FL',
                'georgia': 'GA',
                'guam': 'GU',
                'hawaii': 'HI',
                'idaho': 'ID',
                'illinois': 'IL',
                'indiana': 'IN',
                'iowa': 'IA',
                'kansas': 'KS',
                'kentucky': 'KY',
                'louisiana': 'LA',
                'maine': 'ME',
                'maryland': 'MD',
                'massachusetts': 'MA',
                'michigan': 'MI',
                'minnesota': 'MN',
                'mississippi': 'MS',
                'missouri': 'MO',
                'montana': 'MT',
                'nebraska': 'NE',
                'nevada': 'NV',
                'new hampshire': 'NH',
                'new jersey': 'NJ',
                'new mexico': 'NM',
                'new york': 'NY',
                'north carolina': 'NC',
                'north dakota': 'ND',
                'northern mariana islands': 'MP',
                'ohio': 'OH',
                'oklahoma': 'OK',
                'oregon': 'OR',
                'pennsylvania': 'PA',
                'puerto rico': 'PR',
                'rhode island': 'RI',
                'south carolina': 'SC',
                'south dakota': 'SD',
                'tennessee': 'TN',
                'texas': 'TX',
                'utah': 'UT',
                'vermont': 'VT',
                'virgin islands': 'VI',
                'virginia': 'VA',
                'washington': 'WA',
                'west virginia': 'WV',
                'wisconsin': 'WI',
                'wyoming': 'WY'
            }
            self.assistant_message("The city name?")
            self.speak("The city name?")
            city1 = self.takeCommand().lower()
            s = True
            while s == True:
                self.assistant_message("The state name?")
                self.speak("The state name?")
                state = self.takeCommand().lower()
                if state in us_state_abbrev:
                    s == False
                    shortform = us_state_abbrev[state]
                    try:
                        webbrowser.open(
                            "https://www.fandango.com/"+city1+'_'+shortform+'_movietimes')
                    except:
                        self.assistant_message("Could not open the website")
                    break


        # If user wants to open drexel
        elif 'drexel' in query:
            try:
                webbrowser.open(
                    f'https://one.drexel.edu/')

            except Exception as e:
                self.assistant_message("Unable to access Drexel University site at this time")
                self.speak("Error opening Drexel University")

        # If user wants to open ebay
        elif 'open ebay' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://ebay.com/')

            except Exception as e:
                webbrowser.open(
                    f'https://ebay.com/')

        # If user wants to open some product on ebay
        elif 'on ebay' in query:
            query = query.replace("on ebay", "")
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
            f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={query}&_sacat=0')

            except Exception as e:
                webbrowser.open(
                    f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={query}&_sacat=0')


        # If user wants to open python docs
        elif 'python' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://python.org/')

            except Exception as e:
                webbrowser.open(
                    f'https://python.org/')

        # If user wants to open whatsapp
        elif 'open whatsapp' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://web.whatsapp.com/')

            except Exception as e:
                webbrowser.open(
                    f'https://web.whatsapp.com/')

        # If user wants to open something on youtube
        elif 'on youtube' in query:
            query = query.replace("on youtube", "")
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://www.youtube.com/results?search_query={query}')

            except Exception as e:
                webbrowser.open(
                    f'https://www.youtube.com/results?search_query={query}')

        # If user wants to open discord
        elif 'open discord' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://discord.com/channels/@me')

            except Exception as e:
                webbrowser.open('https://discord.com/channels/@me')

        # If user wants to open instagram
        elif 'open instagram' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(f'https://www.instagram.com')

            except Exception as e:
                webbrowser.open('https://www.instagram.com')

        # If user wants to open linkedin
        elif 'open linkedin' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(f'https://www.linkedin.com')

            except Exception as e:
                webbrowser.open('https://www.linkedin.com')

        # If user wants to open slack
        elif 'open slack' in query:
            # try to open Slack
            try:
                self.assistant_message("Opening Slack")
                self.speak("Opening Slack")
                webbrowser.open('https://slack.com')
            except:  # Runs except when needed
                self.assistant_message("Unable to access Slack at this time")
                self.speak("Error opening slack")

        # If user wants to open spotify
        elif 'open spotify' in query:
            # try to open Spotify
            try:
                self.assistant_message("Opening Spotify")
                self.speak("Opening Spotify")
                webbrowser.open('https://www.spotify.com/us/')

            except:  # Runs except when needed
                self.assistant_message("Unable to access Spotify at this time")
                self.speak("Error opening spotify")

        # If user wants to open youtube
        elif 'open youtube' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(f'https://www.youtube.com')

            except Exception as e:
                webbrowser.open('https://www.youtube.com')

        # If user wants to open amazon
        elif 'open amazon' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(f'https://www.amazon.com')

            except Exception as e:
                webbrowser.open('https://www.amazon.com')


        # If user wants to open some product on amazon
        elif 'on amazon' in query:
            query = query.replace("on amazon", "")
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://www.amazon.in/s?k={query}&ref=nb_sb_noss')

            except Exception as e:
                webbrowser.open(
                    f'https://www.amazon.in/s?k={query}&ref=nb_sb_noss')

        # If user wants to remind him/herself
        elif 'reminder' in query:
            query = query.replace("reminder", "")
            query = query.lstrip()
            query = query.split("/")
            if len(query) != 3:
                self.assistant_message(
                    "Error encountered. Please enter in date format day/month/year")
                self.speak(
                    "Error encountered. Please enter in date format day/month/year")

            else:
                try:
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                        "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(
                        f'https://calendar.google.com/calendar/u/0/r/day/{query[2]}/{query[1]}/{query[0]}')

                except Exception as e:
                    webbrowser.open(
                        f'https://calendar.google.com/calendar/u/0/r/day/{query[2]}/{query[1]}/{query[0]}')


        # If user wants to open zoom
        elif 'open zoom' in query:
            try:
                zoom_path = 'C:\\Users\\Ansh\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
                self.speak("Opening Zoom;..... Sir")
                os.startfile(zoom_path)

            except Exception as e:
                webbrowser.open('https://www.zoom.us')

        # elif 'cs50' in query:
            # pass

        # If user thanks Oliver
        elif 'thank you' in query or 'thanks' in query:
            self.assistant_message("Very welcome")
            self.speak("Very welcome")

        # If user wants to open something on google
        elif 'on google' in query:
            query = query.replace("on google", "")
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://www.google.com/search?q={query}')

            except Exception as e:
                webbrowser.open(f'https://www.google.com/search?q={query}')


        # If the user wants to open google
        elif 'open google' in query:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(f'https://www.google.com')

            except Exception as e:
                webbrowser.open(f'https://www.google.com')


        # If the user asks Oliver
        elif 'where are you' in query:
            self.assistant_message("With you")
            self.speak("With you")

        # Simple gestures from Oliver
        elif 'how are you' in query:
            self.assistant_message("I am always in the pink of health!")
            self.speak("I am always in the pink of health!")

        # If user wants to play games
        elif 'games' in query:
            import random
            self.assistant_message("Activating Magic 8-ball game...")
            self.speak("Activating Magic 8-ball game...")
            self.assistant_message(
                "Throw me some questions! and to quit speak 'exit'")
            self.speak("Throw me some questions! and to quit speak 'exit'")

            answer_list = ["Probably", "Yes", "I don't think so",
                           "Plausible", "Improbable", "Never", "Definitely"]

            query = self.takeCommand()
            while ("exit" not in query):
                if (query == "None" or query == None or query == "none"):
                    pass
                else:
                    choice = random.choice(answer_list)
                    self.assistant_message(choice)
                    self.speak(choice)

                query = self.takeCommand()

        # If user wants to play quiz
        elif 'trivia' in query:
            import random

            self.assistant_message(
                "Welcome to the trivia game! speak 'exit' to close the game")
            self.speak(
                "Welcome to the trivia game! speak 'exit' to close the game")

            self.assistant_message(
                "Speak Apple for A, Balloon for B, Carrot for C, and Donkey for D")
            self.speak(
                "Speak Apple for A, Balloon for B, Carrot for C, Donkey for D")

            r = requests.get("https://opentdb.com/api.php?amount=100")
            data = eval(r.text)

            questions = data['results']
            answer = "e"
            i = 0

            answers = {"apple": 0, "balloon": 1, "carrot": 2, "donkey": 3}

            while(answer != "exit"):

                i = random.randint(0, 50)

                questions[i]['question'] = questions[i]['question'].replace(
                    "&quot;", "")

                if (questions[i]['type'] == "boolean"):

                    self.assistant_message("\nTrue or False?")
                    self.speak("\nTrue or False?")
                    self.assistant_message(f"{questions[i]['question']}")
                    self.speak(f"{questions[i]['question']}")

                    answer = self.takeCommand().lower()

                    while (answer.lower() != "true" and answer != "false" and answer != "exit"):
                        answer = self.takeCommand().lower()

                    if (answer == questions[i]['correct_answer']):
                        self.assistant_message("Correct Answer!")
                        self.speak("Correct Answer!")

                    elif(answer == "exit"):
                        break

                    else:
                        self.assistant_message("Incorrect Answer!")
                        self.speak("Incorrect Answer!")

                else:
                    self.assistant_message(f"\n{questions[i]['question']}")
                    self.speak(f"\n{questions[i]['question']}")

                    correct_answer = questions[i]['correct_answer']

                    lis = [f"{questions[i]['correct_answer']}", f"{questions[i]['incorrect_answers'][0]}",
                           f"{questions[i]['incorrect_answers'][1]}", f"{questions[i]['incorrect_answers'][2]}"]
                    random.shuffle(lis)
                    option = ["A - ", "B - ", "C - ", "D - "]
                    ind = lis.index(correct_answer)
                    indss = 0
                    for item in lis:
                        self.assistant_message(option[indss] + item)
                        self.speak(option[indss] + item)
                        indss += 1

                    self.assistant_message(
                        "Speak Apple for A, Balloon for B, Carrot for C, Donkey for D, to close the game speak 'exit'")

                    answer = self.takeCommand().lower()

                    while (answer != "apple" and answer != "balloon" and answer != "carrot" and answer != "donkey" and answer != "exit"):
                        answer = self.takeCommand().lower()

                    try:

                        if (answer == "exit"):
                            break

                        elif (answers[answer] == ind):
                            self.assistant_message(f"Correct!")
                            self.speak(f"Correct!")

                        else:
                            self.assistant_message(
                                f"Incorrect, the correct answer was {lis[ind]}")
                            self.speak(
                                f"Incorrect, the correct answer was {lis[ind]}")

                    except Exception as e:
                        self.assistant_message(f"Wrong input! next question")
                        self.speak(f"Wrong input! next question")

            self.assistant_message("Thank you for playing with me!")
            self.speak("Closing trivia mode")


        # If user wants to initiate voice typing
        elif 'voice typing' in query:
            import pyautogui
            self.assistant_message("Activating voice typing...")
            self.speak("Activating voice typing...")
            self.assistant_message("Select your typing area using your mouse")
            self.speak("Select your typing area using your mouse")
            self.assistant_message("Start speaking! and to quit speak 'exit'")
            self.speak("Start speaking! and to quit speak 'exit'")
            query = self.takeCommand()
            while ("exit" not in query):
                if (query == "None" or query == None or query == "none"):
                    pass

                else:
                    pyautogui.write(f" {query} ", interval=0.01)

                query = self.takeCommand()

        # elif 'on stackoverflow' in query:
            # pass

        # If user asks to play
        elif 'play' in query:
            query = query.replace("play", "")
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(
                    f'https://music.youtube.com/search?q={query}')

            except Exception as e:
                webbrowser.open(f'https://music.youtube.com/search?q={query}')

        # If user wants to look at the news
        elif "the news" in query:
            url = (
                'https://newsapi.org/v2/top-headlines?country=us&apiKey=10cfde56a10d47ceb7e50465aba2870d')
            a = requests.get(url)
            text = a.text
            my_json = json.loads(text)
            for i in range(0, 6):
                self.assistant_message(my_json['articles'][i]['title'])
                self.speak(my_json['articles'][i]['title'])
                self.speak("Next news!")

        elif 'the time' in query:
            hour = int(datetime.datetime.now().hour)
            hourss = "PM"
            if (hour < 12):
                hourss = "AM"
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.assistant_message(f"Current Time = {current_time} {hourss}")
            self.speak(f"Current time is {current_time} {hourss}")

        # elif 'open code' in query:
            # pass

        # If user wants to create a file
        elif 'create' in query:
            query = query.replace("create", "")
            query = query.replace("file", "")
            query = query.lstrip()
            new_f = open(query, "x")
            new_f.close()

        # If user wants to convert units
        elif 'convert' in query or 'conversion' in query:

            import platform

            self.assistant_message(
                'Which unit do you want it converted from:  ')
            self.speak('Which unit do you want it converted from:  ')
            unit1 = self.takeCommand()
            self.assistant_message('Which unit do you want it converted to:  ')
            self.speak('Which unit do you want it converted to:  ')
            unit2 = self.takeCommand()
            self.assistant_message('Enter the value: ')
            self.speak('Enter the value: ')
            num1 = self.takeCommand()

            if unit1 == "cm" and unit2 == "m":
                ans = float(num1)/100
                self.assistant_message(f"{ans}")
                self.speak(f"{ans}")

            elif unit1 == "mm" and unit2 == "cm":
                ans = float(num1)/10
                self.assistant_message(f"{ans} cm")
                self.speak(f"{ans} cm")

            elif unit1 == "m" and unit2 == "cm":
                ans = float(num1)*100
                self.assistant_message(f"{ans} cm")
                self.speak(f"{ans} cm")

            elif unit1 == "cm" and unit2 == "mm":
                ans = float(num1)*10
                self.assistant_message(f"{ans} mm")
                self.speak(f"{ans} mm")

            elif unit1 == "mm" and unit2 == "m":
                ans = float(num1)/1000
                self.assistant_message(f"{ans} m")
                self.speak(f"{ans} m")

            elif unit1 == "m" and unit2 == "mm":
                ans = float(num1)*1000
                self.assistant_message(f"{ans} mm")
                self.speak(f"{ans} mm")

            elif unit1 == "km" and unit2 == "m":
                ans = float(num1)*1000
                self.assistant_message(f"{ans} m")
                self.speak(f"{ans} m")

            elif unit1 == "m" and unit2 == "km":
                ans = float(num1)/1000
                self.assistant_message(f"{ans} km")
                self.speak(f"{ans} km")

            elif unit1 == "mm" and unit2 == "km":
                ans = float(num1)/1000000
                self.assistant_message(f"{ans} km")
                self.speak(f"{ans} km")

            elif unit1 == "ft" and unit2 == "cm":
                ans = float(num1)*30.48
                self.assistant_message(f"{ans} cm")
                self.speak(f"{ans} cm")

            elif unit1 == "ft" and unit2 == "mm":
                ans = float(num1)*304.8
                self.assistant_message(f"{ans} mm")
                self.speak(f"{ans} mm")

            elif unit1 == "ft" and unit2 == "inch":
                ans = float(num1)*12
                self.assistant_message(f"{ans} inch")
                self.speak(f"{ans} inch")

            elif unit1 == "inch" and unit2 == "cm":
                ans = float(num1)*2.54
                self.assistant_message(f"{ans} cm")
                self.speak(f"{ans} cm")

            elif unit1 == "inch" and unit2 == "mm":
                ans = float(num1)*25.4
                self.assistant_message(f"{ans} mm")
                self.speak(f"{ans} mm")

            elif unit1 == "c" and unit2 == "f":
                farhenheit = (float(num1) * 1.8) + 32
                self.assistant_message(f"{farhenheit} farhenheit")
                self.speak(f"{farhenheit} farhenheit")

            elif unit1 == "c" and unit2 == "k":
                kelvin = float(num1) + 273.15
                self.assistant_message(f"{kelvin} kelvin")
                self.speak(f"{kelvin} kelvin")

            elif unit1 == "f" and unit2 == "c":
                celcius = (float(num1)-32)*1.8
                self.assistant_message(f"{celcius} celcius")
                self.speak(f"{celcius} celcius")

            elif unit1 == "f" and unit2 == "k":
                kelvin = (num1-32)*1.8 + 273.15
                self.assistant_message(f"{kelvin} kelvin")
                self.speak(f"{kelvin} kelvin")

            elif unit1 == "k" and unit2 == "c":
                celcius = num1 - 273.15
                self.assistant_message(f"{celcius} celcius")
                self.speak(f"{celcius} celcius")

            elif unit1 == "k" and unit2 == "f":
                farhenheit = ((float(num1) - 273.15) * 1.8) + 32
                self.assistant_message(f"{farhenheit} farhenheit")
                self.speak(f"{farhenheit} farhenheit")

            elif unit1 == "litre" and unit2 == "ml":
                conversion = num1 * 1000
                self.assistant_message(f"{conversion} ml")
                self.speak(f"{conversion} ml")

            elif unit1 == "ml" and unit2 == "litre":
                conversion = num1 / 1000
                self.assistant_message(f"{conversion} l")
                self.speak(f"{conversion} l")

            elif unit1 == "gallons" and unit2 == "litre":
                conversion = num1 * 3.785
                self.assistant_message(f"{conversion} l")
                self.speak(f"{conversion} l")

            elif unit1 == "litre" and unit2 == "gallons":
                conversion = num1 / 3.785
                self.assistant_message(f"{conversion} gallons")
                self.speak(f"{conversion} gallons")

            else:
                self.assistant_message("Wrong input try again")
                self.speak("Wrong input try again")

        # If the user wants to know about the weather
        elif 'weather' in query:
            api_key = "2f01656a7c929d75580b90fc41511e50"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            self.assistant_message("Tell me your city name")
            self.speak("Tell me your city name")

            query = self.takeCommand().lower()

            while (query == None or query == "" or query == "None" or query == "none"):
                query = self.takeCommand().lower()

            Update_url = base_url + "appid=" + api_key + "&q=" + query
            response = requests.get(Update_url)
            pythonformat = response.json()

            if pythonformat["cod"] != "404":
                name = pythonformat["main"]
                current_temperature = name["temp"]
                current_humidiy = name["humidity"]
                Desc = pythonformat["weather"]
                weather_description = Desc[0]["description"]

            # math calcualtion for converting into fahreneit
                cel = current_temperature - 273.15
                fah = cel * (9 / 5) + 32

                self.assistant_message(" Temperature (in Fahrenheit Units) = " + str(fah) +
                                       "\n Humidity =" + str(current_humidiy) +
                                       "\n Description = " + str(weather_description))

                self.speak(" Temperature in Fahrenheit is " + str(fah)[len(str(fah)) % 5] +
                           " the Humidity is " + str(current_humidiy) +
                           " in short, it is " + str(weather_description))

            else:
                self.assistant_message("Sorry, I cannot find the location")
                self.speak("Sorry, I cannot find the location")

        # If the user wants to check the date
        elif 'the date' in query:
            date = datetime.datetime.now()
            self.assistant_message(date.strftime("%m/%d/%Y"))
            self.speak(date.strftime("%m/%d/%Y"))

        # Code to change the name of the user
        elif 'change my name' in query or 'change name' in query or 'call me something else' in query:
            f = open("names.txt", "w")
            self.assistant_message("What do you want to change it to?")
            self.speak("What do you want to change it to?")
            name = self.takeCommand().lower()
            while(name == None or len(name) < 1 or name == "None" or name == "none"):
                name = self.takeCommand().lower()

            f.write(name)
            self.speak("Successfuly changed!")
            self.assistant_message("Successfully changed")
            f.close()

        # TO check user's name
        elif "what's my name" in query or "my name" in query:
            self.assistant_message(f"{name} right?")
            self.speak(f"{name} right?")

        # TO check the battery percentage
        elif 'battery' in query:
            battery = psutil.sensors_battery()
            percent = battery.percent
            self.assistant_message(f"Battery - {percent}%")
            self.speak(f"The battery on your device is {percent}%")

        # TO send email to someone
        elif 'send email to' in query:
            import yagmail
            import keyring
            import getpass
            receiver_email = input("Enter the email you want to send it to:")
            body = input("Enter the body that you want to send:")
            subject_user = input("Enter the subject for your email:")

            e = open("email.txt", "r")
            yag = yagmail.SMTP(e.read())

            # send the email
            try:
                password = getpass.getpass("Enter your password:")
                keyring.set_password("system", f"{e.read()}", f"{password}")
                yag.send(
                    to=receiver_email,
                    subject=subject_user,
                    content=body)

            except Exception as f:
                print(
                    f"Please allow less secure apps to ON by changing your gmail settings. Error{f}")

            e.close()

        # To change email
        elif 'change email' in query or 'change my email' in query:
            self.assistant_message("Enter your new email: ")
            self.speak("Enter your new email")
            new_email = input("Enter your new email: ")
            while(new_email == "" or new_email == "None" or new_email == "none"):
                new_email = input("Can I have your email: ")

            f = open("email.txt", "r+")
            f.write(f"{new_email}")
            print("Sucessfully changed")
            f.close()

        # TO check if email is present
        elif 'email' in query:
            try:
                f = open("email.txt", "r+")
                email = f.read()
                f.close()

            except:
                print(
                    "I don't have your email, can I have it? Please make sure that it is a gmail")
                email = input("Enter your email: ")
                while((email == "") or (email == "None") or (not email.endswith("@gmail.com")) or (email.i.salnum)):
                    email = input(
                        "Please enter your gmail in the proper format (username@gmail.com): ")
                    email = email.strip
                    f = open("email.txt", "x")
                    f.close()
                    g = open("email.txt", "w")
                    g.write(email)
                    g.close()
                    print("Thank you")

        # To get screenshots
        elif 'screenshot' in query or 'screen shot' in query:
            self.assistant_message("Taking screenshot")
            self.speak("Taking screenshot!")
            import pyautogui
            import random
            image = pyautogui.screenshot()
            screenshot = image
            number = random.randint(0, 10000000000000)
            screenshot.save(f'{sys.path[0]}/{number}Oliver_Screenshot.png')
            self.assistant_message(
                f"Screenshot saved at {sys.path[0]}/{number}Oliver_Screenshot.png")
            self.speak("Screenshot saved!")

        # If the user wants to close Oliver
        elif 'goodbye' in query or 'bye' in query or 'quit' == query or 'exit' == query:
            self.assistant_message(
                f"Thank you for your time. Over-and-out, {name}")
            self.speak(
                f"Thank you for your time...;.....Over-and-out...........{name}")
            set_f.close()
            exit()

        else:
            pass

        # Returns the input button to normal state for clicking
        self.bt["state"] = "normal"

    # Function to show user's message on window
    def user_message(self, *message):
        self.tb.insert(END, "You - \n")
        self.tb.insert(END, f"{message[0]}\n\n")
        self.tb.yview(END)
        self.tb.update()

    # Function to show assistant's message on window
    def assistant_message(self, *message):
        if (message[0] != "Recognizing..." and message[0] != "Listening..." and "\r" not in message[0]):
            self.tb.insert(END, "Oliver - \n")

        self.tb.insert(END, f"{message[0]}\n\n")
        self.tb.yview(END)
        self.tb.update()

    # Function to open a command window
    def command_window(self):
        self.new_window = Toplevel()
        self.new_window.geometry("400x400")
        self.new_window.maxsize(600, 600)
        self.new_window.minsize(300, 300)
        self.new_window.title("Oliver | Command Template")
        self.new_window.wm_iconbitmap("logo.ico")
        command_frame = Frame(self.new_window, bg="light blue")
        command_frame.pack(fill="both", expand=True)
        commands = Label(command_frame, text="Voice Commands",
                         font="Calibri 20", bg="light blue2")
        commands.pack(side="top", fill=X)

        TextBBBox = stt.ScrolledText(
            self.new_window, wrap=WORD, bg="snow", font=("Calibri", 14))
        TextBBBox.pack(expand=True, fill=BOTH, anchor='n')

        TextBBBox.insert(END, "'timer' for activating timer\n\n")
        TextBBBox.insert(END, "'drexel' for drexel one website\n\n")
        TextBBBox.insert(END, "'weather' for activating weather report\n\n")
        TextBBBox.insert(END, "'games' for 8-ball game\n\n")
        TextBBBox.insert(END, "'trivia' for quiz game\n\n")
        TextBBBox.insert(END, "'location' for maps\n\n")
        TextBBBox.insert(END, "'{your query} wikipedia' to search on wiki\n\n")
        TextBBBox.insert(
            END, "'{your query} on google' to search on Google\n\n")
        TextBBBox.insert(
            END, "'{your query} on youtube' to search on Youtube\n\n")
        TextBBBox.insert(END, "'battery' to check battery percentage\n\n")
        TextBBBox.insert(END, "'Instagram' to open your Instagram account\n\n")
        TextBBBox.insert(END, "'the date' to look up the date\n\n")
        TextBBBox.insert(END, "'voice typing' to activate voice typing\n\n")
        TextBBBox.insert(END, "'screenshot' to take a screenshot\n\n")
        TextBBBox.insert(
            END, "'reminder {day}/{month}/{year}' to set a reminder\n\n")
        TextBBBox.insert(END, "'the news' to check the news\n\n")


    # Function that takes command from the user
    def takeCommand(self):
        '''
        It takes microphone input form user and string as output
        '''

        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.assistant_message("Listening...")
            r.pause_threshold = 1
            r.phrase_threshold = 0.0
            audio = r.listen(source)

        try:
            self.assistant_message("Recognizing...")
            query = r.recognize_google(audio, language='en-UK')
            self.user_message(f"{query}")

        except Exception as e:
            # print(e)
            self.assistant_message("Sorry, I was not able to understand you\n")
            self.speak("Sorry, I was not able to understand you")
            return "None"

        return query

    # Function that makes Oliver speak
    @staticmethod
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    # Function takes name from the user
    def takename(self):
        # Code to take name of user
        try:
            f = open("names.txt", "r+")
            name = f.read()
            f.close()

        except:
            f = open("names.txt", "x")
            f.close()
            self.assistant_message("Can I have your name?")
            self.speak(
                "I forgot to ask for your name!........ .. ; Can I have your name?")
            name = self.takeCommand().lower()
            while(name == "" or name == "None" or name == "none"):
                name = self.takeCommand().lower()

            g = open("names.txt", "w")
            g.write(name)
            g.close()
            self.assistant_message("Thank you")
            self.speak("Thank you")
        return name


if __name__ == "__main__":
    import pyttsx3
    # engine using pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 178)

    # Code to open settings.txt and put set_f as the global pointer
    try:
        set_f = open("settings.txt", "r+")

    except Exception as e:
        open("settings.txt", "x")
        set_f = open("settings.txt", "w")
        set_f.write("1Text\n")
        set_f.write("#82CFF6\n")
        set_f.close()
        set_f = open("settings.txt", "r+")

    app = GUI()
    app.mainloop()
