def draw_worldempty ():
    from colorama import Back, init
    init(autoreset=True)

    va = Back.LIGHTWHITE_EX + '    '

    ESPACIONEGRO = Back.BLACK + '    '
    PASTO = Back.GREEN + '    '
    AGUA = Back.BLUE + '    '

    mapa = [[va for i in range(32)] for j in range(21)]

    for i in range(len(mapa)):
        if i == 0:
            for j in range(len(mapa[i])):
                mapa[i][j]= str(j)
        for l in range(32):
            if l == 0:
                mapa[i][l] = str(i)

    for y in range(21):
            for x in range(len(mapa[y])):
                if x <= 30:
                    print(mapa[y][x].center(4), end='')
                elif x == 31:
                    print()

draw_worldempty()

