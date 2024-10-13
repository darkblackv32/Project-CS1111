def draw_worldempty ():
    from colorama import Back, init
    init(autoreset=True)



    ESPACIONEGRO = Back.BLACK + '    '
    PASTO = Back.GREEN + '    '
    AGUA = Back.BLUE + '    '

    mapa = [[Back.LIGHTWHITE_EX + '    ' for i in range(32)] for j in range(21)]

    for i in range(len(mapa)):
        if i == 0:
            for j in range(len(mapa[i])):
                mapa[i][j]= str(j)
        for l in range(32):
            if l == 0:
                mapa[i][l] = str(i)
            # La parte negra
        for i in range(14, 21):
                for j in range(30):
                 mapa[i][j + 1] = ESPACIONEGRO
                 tierra = mapa[i][j]

         # la parte verde
        for i in range(13, 14):
         for j in range(30):
                mapa[i][j + 1] = PASTO
                pasto = mapa[i][j + 1]

            # La parte de agua
         for i in range(13, 18):
            for j in range(25, 28):
                mapa[i][j + 1] = AGUA
                lago = mapa[i][j + 1]
        # 1PARTE VERDE DEL PRIMER ARBOL
        mapa[6][5] = Back.GREEN + '    '
        # 2PARTE VERDE DEL PRIMER ARBOL
        mapa[7][4] = Back.GREEN + '    '
        mapa[7][5] = Back.GREEN + '    '
        mapa[7][6] = Back.GREEN + '    '
        # 3PARTE VERDE DEL PRIMER ARBOL
        mapa[8][3] = Back.GREEN + '    '
        mapa[8][4] = Back.GREEN + '    '
        mapa[8][5] = Back.GREEN + '    '
        mapa[8][6] = Back.GREEN + '    '
        mapa[8][7] = Back.GREEN + '    '
        # TALLO DEL PRIMER ARBOL
        mapa[9][5] = Back.RED + '    '
        mapa[10][5] = Back.RED + '    '
        mapa[11][5] = Back.RED + '    '
        mapa[12][5] = Back.RED + '    '

        # 1PARTE VERDE DEL SEGUNDO ARBOL
        mapa[6][11] = Back.GREEN + '    '
        # 2PARTE VERDE DEL SEGUNDO ARBOL
        mapa[7][10] = Back.GREEN + '    '
        mapa[7][11] = Back.GREEN + '    '
        mapa[7][12] = Back.GREEN + '    '
        # 3PARTE VERDE DEL SEGUNDO ARBOL
        mapa[8][9] = Back.GREEN + '    '
        mapa[8][10] = Back.GREEN + '    '
        mapa[8][11] = Back.GREEN + '    '
        mapa[8][12] = Back.GREEN + '    '
        mapa[8][13] = Back.GREEN + '    '
        # TALLO DEL SEGUNDO ARBOL
        mapa[9][11] = Back.RED + '    '
        mapa[10][11] = Back.RED + '    '
        mapa[11][11] = Back.RED + '    '
        mapa[12][11] = Back.RED + '    '

        # 1PARTE VERDE DEL TERCER ARBOL
        mapa[6][17] = Back.GREEN + '    '
        # 2PARTE VERDE DEL TERCER ARBOL
        mapa[7][16] = Back.GREEN + '    '
        mapa[7][17] = Back.GREEN + '    '
        mapa[7][18] = Back.GREEN + '    '
        # 3PARTE VERDE DEL TERCER ARBOL
        mapa[8][15] = Back.GREEN + '    '
        mapa[8][16] = Back.GREEN + '    '
        mapa[8][17] = Back.GREEN + '    '
        mapa[8][18] = Back.GREEN + '    '
        mapa[8][19] = Back.GREEN + '    '
        # TALLO DEL TERCER ARBOL
        mapa[9][17] = Back.RED + '    '
        mapa[10][17] = Back.RED + '    '
        mapa[11][17] = Back.RED + '    '
        mapa[12][17] = Back.RED + '    '

        # 1PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
        mapa[3][22] = Back.GREEN + '    '
        # 2PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
        mapa[4][21] = Back.GREEN + '    '
        mapa[4][22] = Back.GREEN + '    '
        mapa[4][23] = Back.GREEN + '    '
        # 3PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
        mapa[5][20] = Back.GREEN + '    '
        mapa[5][21] = Back.GREEN + '    '
        mapa[5][22] = Back.GREEN + '    '
        mapa[5][23] = Back.GREEN + '    '
        mapa[5][24] = Back.GREEN + '    '
        # 4PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
        mapa[6][19] = Back.GREEN + '    '
        mapa[6][20] = Back.GREEN + '    '
        mapa[6][21] = Back.GREEN + '    '
        mapa[6][22] = Back.GREEN + '    '
        mapa[6][23] = Back.GREEN + '    '
        mapa[6][24] = Back.GREEN + '    '
        mapa[6][25] = Back.GREEN + '    '
        # TALLO DEL CUARTO ARBOL - ARBOL GRANDE
        mapa[7][22] = Back.RED + '    '
        mapa[8][22] = Back.RED + '    '
        mapa[9][22] = Back.RED + '    '
        mapa[10][22] = Back.RED + '    '
        mapa[11][22] = Back.RED + '    '
        mapa[12][22] = Back.RED + '    '

        # 1PARTE VERDE DEL QUINTO ARBOL - ARBOL PEQUEÑO 1
        mapa[8][25] = Back.GREEN + '    '
        # 2PARTE VERDE DEL QUINTO ARBOL - ARBOL PEQUEÑO 1
        mapa[9][24] = Back.GREEN + '    '
        mapa[9][25] = Back.GREEN + '    '
        mapa[9][26] = Back.GREEN + '    '
        # TALLO DEL QUINTO ARBOL . ARBOL PEQUEÑO 1
        mapa[10][25] = Back.RED + '    '
        mapa[11][25] = Back.RED + '    '
        mapa[12][25] = Back.RED + '    '

        # 1PARTE VERDE DEL SEXTO ARBOL - ARBOL PEQUEÑO 2
        mapa[8][29] = Back.GREEN + '    '
        # 2PARTE VERDE DEL SEXTO ARBOL - ARBOL PEQUEÑO 2
        mapa[9][28] = Back.GREEN + '    '
        mapa[9][29] = Back.GREEN + '    '
        mapa[9][30] = Back.GREEN + '    '
        # TALLO DEL SEXTO ARBOL . ARBOL PEQUEÑO 2
        mapa[10][29] = Back.RED + '    '
        mapa[11][29] = Back.RED + '    '
        mapa[12][29] = Back.RED + '    '

        # piedras en parte inferior
        mapa[17][2] = Back.WHITE + '    '
        mapa[14][5] = Back.WHITE + '    '
        mapa[18][5] = Back.WHITE + '    '
        mapa[14][5] = Back.WHITE + '    '
        mapa[16][7] = Back.WHITE + '    '
        mapa[19][7] = Back.WHITE + '    '
        mapa[16][10] = Back.WHITE + '    '
        mapa[19][15] = Back.WHITE + '    '
        mapa[18][23] = Back.WHITE + '    '
        mapa[17][23] = Back.WHITE + '    '
        mapa[16][23] = Back.WHITE + '    '
        mapa[15][23] = Back.WHITE + '    '
        mapa[15][25] = Back.WHITE + '    '
        mapa[19][29] = Back.WHITE + '    '
        # piedras en parte superior
        mapa[12][7] = Back.WHITE + '    '
        mapa[11][7] = Back.WHITE + '    '
        mapa[12][8] = Back.WHITE + '    '
        mapa[11][8] = Back.WHITE + '    '
        mapa[11][9] = Back.WHITE + '    '
        mapa[12][9] = Back.WHITE + '    '
        mapa[10][8] = Back.WHITE + '    '
        mapa[12][12] = Back.WHITE + '    '
        mapa[12][15] = Back.WHITE + '    '
        mapa[12][16] = Back.WHITE + '    '
        mapa[11][16] = Back.WHITE + '    '
        mapa[12][20] = Back.WHITE + '    '
        mapa[12][30] = Back.WHITE + '    '
        #Avatar
        mapa[10][2] = Back.CYAN + '    '
        mapa[11][2] = Back.CYAN + '    '
        mapa[12][2] = Back.CYAN + '    '
        mapa[11][3] = Back.MAGENTA + '    '

        #Sol
        mapa[1][30] = Back.LIGHTYELLOW_EX + '    '
        mapa[2][30] = Back.LIGHTYELLOW_EX + '    '
        mapa[3][30] = Back.LIGHTYELLOW_EX + '    '
        mapa[1][29] = Back.LIGHTYELLOW_EX + '    '
        mapa[2][29] = Back.LIGHTYELLOW_EX + '    '
        mapa[3][29] = Back.LIGHTYELLOW_EX + '    '
        mapa[1][28] = Back.LIGHTYELLOW_EX + '    '
        mapa[2][28] = Back.LIGHTYELLOW_EX + '    '
        mapa[3][28] = Back.LIGHTYELLOW_EX + '    '
        mapa[2][27] = Back.LIGHTYELLOW_EX + '    '
        mapa[4][27] = Back.LIGHTYELLOW_EX + '    '
        mapa[4][29] = Back.LIGHTYELLOW_EX + '    '



    for y in range(21):
            for x in range(len(mapa[y])):
                if x <= 30:
                    print(mapa[y][x].center(4), end='')
                elif x == 31:
                    print()

draw_worldempty()
