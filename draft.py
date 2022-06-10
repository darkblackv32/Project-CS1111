import colorama
colorama.init(autoreset=True)
from colorama import Back, Style, Fore
import numpy as np


def drawworld_empty(a):
    for x in range(20):
        for y in range(30):
            print(Back.LIGHTWHITE_EX + '', end="")
            print(Fore.LIGHTWHITE_EX + ' 0', end="")
        print(Style.RESET_ALL)

drawworld_empty(10)
