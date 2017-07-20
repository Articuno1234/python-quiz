import sys
import os
import time
import random

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def user_choice():
    return input("> ").lower().strip()
  
def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
  
def load():
  times = [1, 2, 3, 4]
  print("Loading... (1%)")
  time.sleep(random.choice(times))
  print("Loading. (50%)")
  time.sleep(random.choice(times))
  print("Loading.. (100%)")
  time.sleep(random.choice(times))
  print("Starting Menu...")
  time.sleep(random.choice(times))
  menu()
  
def menu():
  print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
        "        Python Quiz          \n"
        "-=-=-=-=-=-=-=-=-=-=-=--=-=-=\n")
  print("1. Start\n"
        "\n"
        "0. Exit\n")
  choice = user_choice()
  if choice == "1":
    start()
  if choice == "0":
    clear_screen()
    print("Exited with code 0.1")
    sys.exit(1)
    
def start():
  print("What do you use to say something in terminal?")
  choice = user_choice()
  if choice == "print":
    print("Correct!")
  if choice is not == "print":
    print("Incorrect! :(")
    menu()
