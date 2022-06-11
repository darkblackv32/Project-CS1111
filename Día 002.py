from colorama import Back, Fore, Style, init

init(autoreset=True)

va = Back.LIGHTWHITE_EX + "    "
wh = Back.LIGHTWHITE_EX + "    "
bl = Back.BLACK + "    "
gr = Back.GREEN + "    "
ye = Back.YELLOW + "    "
re = Back.RED + "    "
bu = Back.BLUE + "    "
lb = Back.LIGHTBLACK_EX + "    "
cy = Back.CYAN + "    "
ma = Back.MAGENTA + "    "
def draw_world_empty():
    mapa1 = [[]]
    for i in range(1, 21):
        print('')
        for j in range(1, 31):
            print(Back.WHITE + '   ', end = '')


draw_world_empty()