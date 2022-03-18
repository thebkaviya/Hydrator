import datetime
import time

from playsound import playsound


def notify():
    print(f"{datetime.datetime.now().strftime('%Y/%m/%d %H:%m')}: Time to drink")
    play_notification()


def play_notification():
    playsound("./ienba_notification.wav")


print("""
    Hydrator Copyright (C) 2022 Binula Kavisinghe, Tarith Jayasooriya
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions;
    
    This software uses "Notification" by IENB ( https://freesound.org/people/IENBA/sounds/545495/ ) from freesound licensed under CCBY3.0
""")
play_notification()

while True:
    time.sleep(60*60)
    notify()
