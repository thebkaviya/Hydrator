
from curses import window
import datetime
import time
from tkinter import *
from playsound import playsound

reminder = f"{datetime.datetime.now().strftime('%Y/%m/%d %H:%m')}: Time to drink"
startup_message = """
    Hydrator Copyright (C) 2022 Binula Kavisinghe, Tarith Jayasooriya
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions;
    
    This software uses "Notification" by IENB ( https://freesound.org/people/IENBA/sounds/545495/ ) from freesound licensed under CCBY3.0

    You will hear a tone in every hour
"""

def GUI_Window(text):
    window = Tk()
    window.title("Hydrator (C) 2022")
    window.configure(width=500, height=300)
    window.configure(bg='lightgray')
    text = Label(text)
    text.place(x=250,y=150)
    window.mainloop()
    time.sleep(5)
    window.quit()

def play_notification():
    playsound("./ienba_notification.wav")

def notify(text):
    play_notification()
    GUI_Window(text)
    
play_notification()
GUI_Window(startup_message)

while True:
    time.sleep(60*60)
    notify()
