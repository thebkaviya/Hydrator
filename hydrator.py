import datetime
import time
import PySimpleGUI as sg
from playsound import playsound

sg.theme('Topanga')

now = f"""

{datetime.datetime.now().strftime('%Y/%m/%d %H:%m')}: Time to drink water...      
    

"""
startup_message = """
    Hydrator Copyright (C) 2022 Binula Kavisinghe, Tarith Jayasooriya
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions;
    
    This software uses "Notification" by IENB ( https://freesound.org/people/IENBA/sounds/545495/ ) from freesound licensed under CCBY3.0

    You will hear a tone and see a popup every hour.

    Click OK to continue...
    """

def play_notification():
    playsound("./ienba_notification.wav")

def notify():
    sg.popup_timed(now, title = "Hydrator", auto_close_duration = 10, keep_on_top = True, font = ["Calibri",20], non_blocking = True)
    play_notification()

def startup_window():
    play_notification()
    layout = [  [sg.Text(startup_message)], 
                [sg.Button('Ok')] ]
    window = sg.Window('Hydrator (C) 2022', layout,)
    window.read()
    window.close()

startup_window()

while True:
    if datetime.datetime.now().strftime("%M:%S") == "00:00":
        notify()
