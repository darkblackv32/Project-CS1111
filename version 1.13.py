from colorama import Back, init

init(autoreset=True)
world = [[Back.LIGHTWHITE_EX + '    ' for i in range(32)] for j in range(21)]
ESPACIONEGRO = Back.BLACK + '    '
PASTO = Back.GREEN + '    '
AGUA = Back.BLUE + '    '

print()


def draw_worldempty():
    for i in range(len(world)):
        if i == 0:
            for j in range(len(world[i])):
                world[i][j] = str(j)
        for l in range(32):
            if l == 0:
                world[i][l] = str(i)







def draw_world():

        draw_player()

       # La parte negra
        for i in range(14, 21):
          for j in range(30):
             world[i][j + 1] = ESPACIONEGRO
             tierra = world[i][j]

        # la parte verde
        for i in range(13, 14):
            for j in range(30):
                world[i][j + 1] = PASTO
                pasto = world[i][j + 1]

            # La parte de agua
            for i in range(13, 18):
                for j in range(25, 28):
                    world[i][j + 1] = AGUA
                    lago = world[i][j + 1]
        # 1PARTE VERDE DEL PRIMER ARBOL
        world[6][5] = Back.GREEN + '    '
        # 2PARTE VERDE DEL PRIMER ARBOL
        world[7][4] = Back.GREEN + '    '
        world[7][5] = Back.GREEN + '    '
        world[7][6] = Back.GREEN + '    '
        # 3PARTE VERDE DEL PRIMER ARBOL
        world[8][3] = Back.GREEN + '    '
        world[8][4] = Back.GREEN + '    '
        world[8][5] = Back.GREEN + '    '
        world[8][6] = Back.GREEN + '    '
        world[8][7] = Back.GREEN + '    '
        # TALLO DEL PRIMER ARBOL
        world[9][5] = Back.RED + '    '
        world[10][5] = Back.RED + '    '
        world[11][5] = Back.RED + '    '
        world[12][5] = Back.RED + '    '

        # 1PARTE VERDE DEL SEGUNDO ARBOL
        world[6][11] = Back.GREEN + '    '
        # 2PARTE VERDE DEL SEGUNDO ARBOL
        world[7][10] = Back.GREEN + '    '
        world[7][11] = Back.GREEN + '    '
        world[7][12] = Back.GREEN + '    '
        # 3PARTE VERDE DEL SEGUNDO ARBOL
        world[8][9] = Back.GREEN + '    '
        world[8][10] = Back.GREEN + '    '
        world[8][11] = Back.GREEN + '    '
        world[8][12] = Back.GREEN + '    '
        world[8][13] = Back.GREEN + '    '
        # TALLO DEL SEGUNDO ARBOL
        world[9][11] = Back.RED + '    '
        world[10][11] = Back.RED + '    '
        world[11][11] = Back.RED + '    '
        world[12][11] = Back.RED + '    '

        # 1PARTE VERDE DEL TERCER ARBOL
        world[6][17] = Back.GREEN + '    '
        # 2PARTE VERDE DEL TERCER ARBOL
        world[7][16] = Back.GREEN + '    '
        world[7][17] = Back.GREEN + '    '
        world[7][18] = Back.GREEN + '    '
        # 3PARTE VERDE DEL TERCER ARBOL
        world[8][15] = Back.GREEN + '    '
        world[8][16] = Back.GREEN + '    '
        world[8][17] = Back.GREEN + '    '
        world[8][18] = Back.GREEN + '    '
        world[8][19] = Back.GREEN + '    '
        # TALLO DEL TERCER ARBOL
        world[9][17] = Back.RED + '    '
        world[10][17] = Back.RED + '    '
        world[11][17] = Back.RED + '    '
        world[12][17] = Back.RED + '    '

        # 1PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
        world[3][22] = Back.GREEN + '    '
        # 2PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
        world[4][21] = Back.GREEN + '    '
        world[4][22] = Back.GREEN + '    '
        world[4][23] = Back.GREEN + '    '
        # 3PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
        world[5][20] = Back.GREEN + '    '
        world[5][21] = Back.GREEN + '    '
        world[5][22] = Back.GREEN + '    '
        world[5][23] = Back.GREEN + '    '
        world[5][24] = Back.GREEN + '    '
        # 4PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
        world[6][19] = Back.GREEN + '    '
        world[6][20] = Back.GREEN + '    '
        world[6][21] = Back.GREEN + '    '
        world[6][22] = Back.GREEN + '    '
        world[6][23] = Back.GREEN + '    '
        world[6][24] = Back.GREEN + '    '
        world[6][25] = Back.GREEN + '    '
        # TALLO DEL CUARTO ARBOL - ARBOL GRANDE
        world[7][22] = Back.RED + '    '
        world[8][22] = Back.RED + '    '
        world[9][22] = Back.RED + '    '
        world[10][22] = Back.RED + '    '
        world[11][22] = Back.RED + '    '
        world[12][22] = Back.RED + '    '

        # 1PARTE VERDE DEL QUINTO ARBOL - ARBOL PEQUEÑO 1
        world[8][25] = Back.GREEN + '    '
        # 2PARTE VERDE DEL QUINTO ARBOL - ARBOL PEQUEÑO 1
        world[9][24] = Back.GREEN + '    '
        world[9][25] = Back.GREEN + '    '
        world[9][26] = Back.GREEN + '    '
        # TALLO DEL QUINTO ARBOL . ARBOL PEQUEÑO 1
        world[10][25] = Back.RED + '    '
        world[11][25] = Back.RED + '    '
        world[12][25] = Back.RED + '    '

        # 1PARTE VERDE DEL SEXTO ARBOL - ARBOL PEQUEÑO 2
        world[8][29] = Back.GREEN + '    '
        # 2PARTE VERDE DEL SEXTO ARBOL - ARBOL PEQUEÑO 2
        world[9][28] = Back.GREEN + '    '
        world[9][29] = Back.GREEN + '    '
        world[9][30] = Back.GREEN + '    '
        # TALLO DEL SEXTO ARBOL . ARBOL PEQUEÑO 2
        world[10][29] = Back.RED + '    '
        world[11][29] = Back.RED + '    '
        world[12][29] = Back.RED + '    '

        # piedras en parte inferior
        world[17][2] = Back.WHITE + '    '
        world[14][5] = Back.WHITE + '    '
        world[18][5] = Back.WHITE + '    '
        world[14][5] = Back.WHITE + '    '
        world[16][7] = Back.WHITE + '    '
        world[19][7] = Back.WHITE + '    '
        world[16][10] = Back.WHITE + '    '
        world[19][15] = Back.WHITE + '    '
        world[18][23] = Back.WHITE + '    '
        world[17][23] = Back.WHITE + '    '
        world[16][23] = Back.WHITE + '    '
        world[15][23] = Back.WHITE + '    '
        world[15][25] = Back.WHITE + '    '
        world[19][29] = Back.WHITE + '    '
        # piedras en parte superior
        world[12][7] = Back.WHITE + '    '
        world[11][7] = Back.WHITE + '    '
        world[12][8] = Back.WHITE + '    '
        world[11][8] = Back.WHITE + '    '
        world[11][9] = Back.WHITE + '    '
        world[12][9] = Back.WHITE + '    '
        world[10][8] = Back.WHITE + '    '
        world[12][12] = Back.WHITE + '    '
        world[12][15] = Back.WHITE + '    '
        world[12][16] = Back.WHITE + '    '
        world[11][16] = Back.WHITE + '    '
        world[12][20] = Back.WHITE + '    '
        world[12][30] = Back.WHITE + '    '

        # Sol
        world[1][30] = Back.LIGHTYELLOW_EX + '    '
        world[2][30] = Back.LIGHTYELLOW_EX + '    '
        world[3][30] = Back.LIGHTYELLOW_EX + '    '
        world[1][29] = Back.LIGHTYELLOW_EX + '    '
        world[2][29] = Back.LIGHTYELLOW_EX + '    '
        world[3][29] = Back.LIGHTYELLOW_EX + '    '
        world[1][28] = Back.LIGHTYELLOW_EX + '    '
        world[2][28] = Back.LIGHTYELLOW_EX + '    '
        world[3][28] = Back.LIGHTYELLOW_EX + '    '
        world[2][27] = Back.LIGHTYELLOW_EX + '    '
        world[4][27] = Back.LIGHTYELLOW_EX + '    '
        world[4][29] = Back.LIGHTYELLOW_EX + '    '





def draw_player():


    # Avatar
    world[10][2] = Back.CYAN + '    '
    world[11][2] = Back.CYAN + '    '
    world[12][2] = Back.CYAN + '    '
    world[11][3] = Back.MAGENTA + '    '




def move_player(option):
    draw_world()
    draw_worldempty()
    moves = option.split()

    xi = 3  # indicador horizontal de jugador
    xm = 2  # medio del jugador
    xb = 2  # piernas
    xc = 2  # cabeza
    yi = 11  # indicador vertical del jugador
    ym = 11
    yb = 12
    yc = 10

    for i in moves:

        if i == 'right':
            xi = xi + 1  # indicador horizontal de jugador
            xm = xm + 1  # medio del jugador
            xb = xb + 1  # piernas
            xc = xc + 1  # cabeza
        elif i == 'left':
            xi = xi - 1  # indicador horizontal de jugador
            xm = xm - 1  # medio del jugador
            xb = xb - 1  # piernas
            xc = xc - 1
        elif i == 'down':
            yi = yi + 1  # indicador horizontal de jugador
            ym = ym + 1  # medio del jugador
            yb = yb + 1  # piernas
            yc = yc + 1  # cabeza
        elif i == 'up':
            yi = yi - 1  # indicador horizontal de jugador
            ym = ym - 1  # medio del jugador
            yb = yb - 1  # piernas
            yc = yc - 1  # cab

    world[10][2] = Back.LIGHTWHITE_EX + '    '
    world[11][2] = Back.LIGHTWHITE_EX + '    '
    world[12][2] = Back.LIGHTWHITE_EX + '    '
    world[11][3] = Back.LIGHTWHITE_EX + '    '

    if xm in range(1, 31) and xi in range(1, 31) and yb in range(1, 21) and yc in range(1, 21):
        world[yi][xi] = Back.MAGENTA + '    '
        world[ym][xm] = Back.CYAN + '    '
        world[yb][xb] = Back.CYAN + '    '
        world[yc][xc] = Back.CYAN + '    '
    for y in range(21):
        for x in range(len(world[y])):
            if x <= 30:
                print(world[y][x].center(4), end='')
            elif x == 31:
                print()




    else:
        print("Invalid operation")








d = input('$ ')
if d == 'init':

 option = input()
 print('$Welcome to minecraft world XYZ')


 move_player(option)

