import pygame
import time
import datetime
import os

pygame.mixer.init()
time.sleep(1)  # Adding a small delay to ensure mixer is initialized

end_sound = pygame.mixer.Sound('end.wav')

def cntdw(h, m, s):
    full_seconds = h * 3600 + m * 60 + s

    while full_seconds > 0:
        timerApp = datetime.timedelta(seconds=full_seconds)
        os.system("clear")
        print(timerApp, end="\r")
        time.sleep(1)
        full_seconds -= 1

    print("Time's up!")
    end_sound.play()
    pygame.time.wait(int(end_sound.get_length() * 1000))

hours = input("Enter hours: ")
minutes = input("Enter minutes: ")
seconds = input("Enter seconds: ")
cntdw(int(hours), int(minutes), int(seconds))

