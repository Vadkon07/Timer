import time
import datetime
import os

def cntdw(h, m, s):
    full_seconds = h * 3600 + m * 60 + s
 
    while full_seconds > 0:
        timerApp = datetime.timedelta(seconds = full_seconds)
        os.system("clear")
        print(timerApp, end="\r")
        time.sleep(1)
        full_seconds -= 1
 
    print("Time's up!")
 
hours = input("Enter hours: ")
minutes = input("Enter minutes: ")
seconds = input("Enter seconds: ")
cntdw(int(hours), int(minutes), int(seconds))
