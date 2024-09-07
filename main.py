import pygame
import time
import datetime
import os
import json

os.system("clear")

print("Welcome to the Simple Timer!\n")

ask = input("Enter '1' to run a normal timer, enter '2' to run a Pomodoro timer, enter '3' to run presets menu: ")

def cntdw(h, m, s):
    full_seconds = h * 3600 + m * 60 + s
    while full_seconds > 0:
        timerApp = datetime.timedelta(seconds=full_seconds)
        print(timerApp, end="\r")
        time.sleep(1)
        full_seconds -= 1
        os.system("clear")

def load_presets():
    with open('presets.json', 'r') as file:
        return json.load(file)

presets = load_presets()

if ask == '1':
    hours = input("Enter hours: ")
    minutes = input("Enter minutes: ")
    seconds = input("Enter seconds: ")
    cntdw(int(hours), int(minutes), int(seconds))

    pygame.mixer.init()
    time.sleep(1)
    end_sound = pygame.mixer.Sound('end.wav')
    print("Time's up!")
    end_sound.play()
    pygame.time.wait(int(end_sound.get_length() * 1000))

elif ask == '2':
    loop = 1
    while loop == 1:
        # START
        work_time = presets["pomodoro"]
        cntdw(work_time["hours"], work_time["minutes"], work_time["seconds"])

        pygame.mixer.init()
        time.sleep(1)
        end_sound = pygame.mixer.Sound('end.wav')
        print("Time's up!")
        end_sound.play()
        pygame.time.wait(int(end_sound.get_length() * 1000))

        # BREAK
        break_time = presets["pomodoro_break"]
        cntdw(break_time["hours"], break_time["minutes"], break_time["seconds"])

        pygame.mixer.init()
        time.sleep(1)
        end_sound = pygame.mixer.Sound('end.wav')
        print("Time's up!")
        end_sound.play()
        pygame.time.wait(int(end_sound.get_length() * 1000))

elif ask == '3':
    print("--- PRESETS MENU ---\n")
    print("1. Add new preset")
    print("2. Delete preset")
    print("3. Run preset")
    choice = input("Enter your choice: ")

    if choice == '1':
        preset_name = input("Enter preset name: ")
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        presets[preset_name] = {"hours": hours, "minutes": minutes, "seconds": seconds}
        with open('presets.json', 'w') as file:
            json.dump(presets, file, indent=4)
        print(f"Preset '{preset_name}' added successfully!")

    elif choice == '2':
        preset_name = input("Enter preset name to delete: ")
        if preset_name in presets:
            del presets[preset_name]
            with open('presets.json', 'w') as file:
                json.dump(presets, file, indent=4)
            print(f"Preset '{preset_name}' deleted successfully!")
        else:
            print(f"Preset '{preset_name}' not found!")

    elif choice == '3':
        preset_name = input("Enter preset name to run: ")
        if preset_name in presets:
            preset = presets[preset_name]
            cntdw(preset["hours"], preset["minutes"], preset["seconds"])

            pygame.mixer.init()
            time.sleep(1)
            end_sound = pygame.mixer.Sound('end.wav')
            print("Time's up!")
            end_sound.play()
            pygame.time.wait(int(end_sound.get_length() * 1000))
        else:
            print(f"Preset '{preset_name}' not found!")
