import subprocess
import os
from colorama import *



def example_color():
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')


def kill_font():
    subprocess.call("cls", shell=True)


def start():
    while True:
        input_command = input(Fore.YELLOW + Back.BLUE + " " + os.getcwd() + " " + Back.GREEN + Fore.RED + " ===>  " + Back.MAGENTA + Fore.WHITE + " $ " + Style.RESET_ALL + "  ")
        
        if input_command == "clear":
            subprocess.call("cls", shell=True)
        elif input_command == "exit":
            break
        else: 
            subprocess.call(input_command, shell=True)



kill_font()
start()