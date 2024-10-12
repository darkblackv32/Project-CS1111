import colorama
colorama.init(autoreset=True)
from colorama import Back, Style, Fore, init
import numpy as np
init(autoreset=True)

def draw_worldempty ():
    world = [[Back.LIGHTWHITE_EX + '     ' for j in range(1, 31)] for i in range(1, 22)]
    world = np.array(world)
    d = " "
    r = 0
    world[0] = [i for i in range(1, 31)]
    for i in range(1, len(world)):
        r = r + 1
        for j in range(1, len(world[0])):
            world[i][0] = r
    print(d, '   \n'.join([''.join(['{:4}'.format(columna) for columna in fila])for fila in world]))


draw_worldempty()
