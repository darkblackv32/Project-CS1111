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
    mapa1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(21):
        if i == 0:
            for j in range(32):
                if j == 0:
                    mapa1[i].append(" ")
                elif 0 < j <= 31:
                    mapa1[i].append(str(j))
        elif i < 30:
            for j in range(32):
                if j == 0:
                    mapa1[i].append(str(i))
                elif j <= 31:
                    mapa1[i].append(va)

    for y in range(21):
        for x in range(len(mapa1[y])):
            if x <= 30:
                print(mapa1[y][x].center(4), end='')
            elif x == 31:
                print()
    return mapa1
draw_world_empty()
