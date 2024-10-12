from colorama import Back, init

init(autoreset=True)
world = [[Back.LIGHTWHITE_EX + '    ' for i in range(32)] for j in range(21)] # matriz por comprension, representa
# 20x 30 y ponemos 32 para poner los numeros y 31- 1 y 21-1 nos da 30 y
# 20, 30 x 20
ESPACIONEGRO = Back.BLACK + '    ' # variables que usaremos mas tarde para determinar un pixel negro, azul y verde
PASTO = Back.GREEN + '    '
AGUA = Back.BLUE + '    '

print() # para que tenga orden



def draw_worldempty():
    for i in range(len(world)):  # recorremos las filas de la matriz con len
        if i == 0:
            for j in range(len(world[i])):  # selecciona todos los elementos de esas fila
                world[i][j] = str(j)  # cada uno se convierte en un string
        for l in range(32):  # seleccionar a los primeros valores de cada fila, si l es 0 entonces vemos que es la
            # primera
            if l == 0:
                world[i][l] = str(i)  # i representa a todas las filas y l representa al primer elementos de cada
                # fila y entonces
                # seleccionamos a todos los primeros elementos de cada fila para convertirlos


def draw_world(): # seleccionamos las filas que queremos pintar y el numero de columnas que pintaremos, y cambiamos
    # los pixeles balncos según el color que corresponda
    # La parte negra
    for i in range(14, 21):
        for j in range(30):
            world[i][j + 1] = ESPACIONEGRO # j + 1 es para evitar que se pinten los numeros
            tierra = world[i][j]

    # la parte verde
    for i in range(13, 14):
        for j in range(30):
            world[i][j + 1] = PASTO
            pasto = world[i][j + 1] # j + 1 es para evitar que se pinten los numeros

        # La parte de agua
        for i in range(13, 18):
            for j in range(25, 28):
                world[i][j + 1] = AGUA
                lago = world[i][j + 1] # j + 1 es para evitar que se pinten los numeros
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


def draw_player(xi, yi, xm, ym, xb, yb, xc, yc):   # Mismo proceso que el anterior para dibujar al avatar

    # Avatar
    world2 = world
    world2[yi][xi] = Back.MAGENTA + '    ' # la mano
    world2[ym][xm] = Back.CYAN + '    '  # centro
    world2[yb][xb] = Back.CYAN + '    ' # pies
    world2[yc][xc] = Back.CYAN + '    ' # cabeza

def collect(option, zx, zy):

    countwood = 0 #inicia la cuenta en 0
    countrock = 0
    xi = 3 + zx  #indicadores de la mano del jugador
    yi = 11 + zy #recibe el zx y el zy para que collect se ejecute siempre en el espacio
    #de la mano del jugador sin importar el numero de comandos


    #Verifica que la mano del jugador se encuentra en el mismo espacio que un arbol
    if world[yi][xi] == world[9][5] or world[yi][xi] == world[10][5] or world[yi][xi] == world[11][5] or world[yi][xi] == world[12][5]:
        world[yi][xi] = Back.LIGHTWHITE_EX + '    '
        countwood += 1
    elif world[yi][xi] == world[9][5] or world[yi][xi] == world[10][5] or world[yi][xi] == world[11][5] or world[yi][xi] == world[12][5]:
        world[yi][xi] = Back.LIGHTWHITE_EX + '    '
        countwood += 1
    elif world[yi][xi] == world[10][29] or world[yi][xi] == world[11][29] or world[yi][xi] == world[12][29]:
        world[yi][xi] = Back.LIGHTWHITE_EX + '    '
        countwood += 1
    elif world[yi][xi] == world[10][25] or world[yi][xi] == world[11][25] or world[yi][xi] == world[12][25]:
        world[yi][xi] = Back.LIGHTWHITE_EX + '    '
        countwood += 1
    elif world[yi][xi] == world[7][22] or world[yi][xi] == world[8][22] or world[yi][xi] == world[9][22] or world[yi][xi] == world[10][22] or world[yi][xi] == world[11][22] or world[yi][xi] == world[12][22]:
        world[yi][xi] = Back.LIGHTWHITE_EX + '    '
        countwood += 1
    elif world[yi][xi] == world[9][17] or world[yi][xi] == world[10][17] or world[yi][xi] == world[11][17] or world[yi][xi] == world[12][17]:
        world[yi][xi] = Back.LIGHTWHITE_EX + '    '
        countwood += 1
    elif world[yi][xi] == world[9][11] or world[yi][xi] == world[10][11] or world[yi][xi] == world[11][11] or world[yi][xi] == world[12][11]:
        world[yi][xi] = Back.LIGHTWHITE_EX + '    '
        countwood += 1
    # Verifica que la mano del jugador se encuentra en el mismo espacio que una piedra
    elif world[yi][xi] == world[12][7] or world[yi][xi] == world[11][7] or world[yi][xi] == world[12][8] or world[yi][xi] == world[11][8] or world[yi][xi] == world[11][9] or world[yi][xi] == world[12][9] or world[yi][xi] == world[10][8] or world[yi][xi] == world[12][12] or world[yi][xi] == world[12][15] or world[yi][xi] == world[12][16] or world[yi][xi] == world[11][16] or world[yi][xi] == world[12][20] or world[yi][xi] == world[12][30]:
        world[yi][xi] = Back.LIGHTWHITE_EX + '    '
        countrock += 1
    #Retorna el contador de los bloques destruidos
    return countwood, countrock


def move_player2(wood, rock): #Recibe los valores en el modulo para guardar la cuenta de collect
    option = ''
    zx = 0
    zy = 0
    draw_world() # llamamos a las funciones anteriores porque nos serviran pora que se ejecute
    draw_worldempty()
    #hacemos un bucle para jugar el tiempo deseado
    while option != 'no':
        draw_world()
        draw_worldempty()
        world2 = world
        option = input('$ ') #aqui recibe los comandos en una string
        moves = option.split()  #se convierte el string en una lsita para manejarla

        xi = 3 + zx  # indicador x de la mano del jugador
        xm = 2 + zx  # indicador x del medio del jugador
        xb = 2 + zx  # indicador x de los pies del jugador
        xc = 2 + zx  # indicador x de la cabeza del jugador
        yi = 11 + zy # indicador y de la mano del jugador
        ym = 11 + zy # indicador y del medio  del jugador
        yb = 12 + zy # indicador y de los pies del jugador
        yc = 10 + zy # indicador y de la cabeza del jugador


        #aqui se cambian las coordenadas de los pixeles del cuerpo del jugador para poder moverlo despues
        for i in moves:
            if i == 'right':
                # es necesario para que el jugador no tenga un clon
                world2[yi][xi] = Back.LIGHTWHITE_EX + '    '
                world2[ym][xm] = Back.LIGHTWHITE_EX + '    '
                world2[yb][xb] = Back.LIGHTWHITE_EX + '    '
                world2[yc][xc] = Back.LIGHTWHITE_EX + '    '
                xi = xi + 1
                xm = xm + 1
                xb = xb + 1
                xc = xc + 1
                zx = zx + 1
            elif i == 'left':
                # es necesario para que el jugador no tenga un clon
                world2[yi][xi] = Back.LIGHTWHITE_EX + '    '
                world2[ym][xm] = Back.LIGHTWHITE_EX + '    '
                world2[yb][xb] = Back.LIGHTWHITE_EX + '    '
                world2[yc][xc] = Back.LIGHTWHITE_EX + '    '
                xi = xi - 1
                xm = xm - 1
                xb = xb - 1
                xc = xc - 1
                zx = zx - 1
            elif i == 'down':
                # es necesario para que el jugador no tenga un clon
                world2[yi][xi] = Back.LIGHTWHITE_EX + '    '
                world2[ym][xm] = Back.LIGHTWHITE_EX + '    '
                world2[yb][xb] = Back.LIGHTWHITE_EX + '    '
                world2[yc][xc] = Back.LIGHTWHITE_EX + '    '
                yi = yi + 1
                ym = ym + 1
                yb = yb + 1
                yc = yc + 1
                zy = zy + 1
            elif i == 'top':
                # es necesario para que el jugador no tenga un clon
                world2[yi][xi] = Back.LIGHTWHITE_EX + '    '
                world2[ym][xm] = Back.LIGHTWHITE_EX + '    '
                world2[yb][xb] = Back.LIGHTWHITE_EX + '    '
                world2[yc][xc] = Back.LIGHTWHITE_EX + '    '
                yi = yi - 1
                ym = ym - 1
                yb = yb - 1
                yc = yc - 1
                zy = zy - 1


        draw_world() #se llama a draw_world para restaurar las partes blancas dejadas cuando se elimina el clon

        if "extract" in option: #se llama a la funcion colect se si se ingreso el comando extract
            collect(option, zx, zy)
            wood = wood + collect(option, zx, zy)[0] #guarda la cuenta de cada bucle
            rock = rock + collect(option, zx, zy)[1]
        if "destroy" in option: #se llama a la funcion destroy se si se ingreso el comando destroy
            destroy(xi, yi)
        if xm in range(1, 31) and xi in range(1, 31) and yb in range(1, 21) and yc in range(1, 21): # se verifica
            # que el jugador este dentro del mundo
            world2[yi][xi] = Back.MAGENTA + '    '  #Se dibuja al jugador dentro del mundo
            draw_player(xi, yi, xm, ym, xb, yb, xc, yc)
            print('$ Welcome to minecraft world XYZ')
            for y in range(21): # de aca en adelante imprimimos la matriz
                for x in range(len(world2[y])):
                    if x <= 30:
                        print(world2[y][x].center(4), end='') # para imprimir la matriz, y end para que se haga fila
                        # y no columna, ya que el
                    elif x == 31:
                        print()
                        break
            print("Wood blocks:", wood)
            print("Stone blocks:", rock)
        else:
            print("Invalid operation") # si el jugador se sale del mundo sale operacion invalida

def destroy(xi, yi):
#coordenadas pasto - parte 1
            # coordenadas pasto - parte 1
            if world[yi][xi] == world[13][1] or world[yi][xi] == world[13][2] or world[yi][xi] == world[13][3] or \
                    world[yi][xi] == world[13][4] or world[yi][xi] == world[13][5] or world[yi][xi] == world[13][6] or \
                    world[yi][xi] == world[13][7] or world[yi][xi] == world[13][8] or world[yi][xi] == world[13][9] or \
                    world[yi][xi] == world[13][10] or world[yi][xi] == world[13][11] or world[yi][xi] == world[13][
                12] or world[yi][xi] == world[13][13] or world[yi][xi] == world[13][14] or world[yi][xi] == world[13][
                15] or world[yi][xi] == world[13][16] or world[yi][xi] == world[13][17] or world[yi][xi] == world[13][
                18] or world[yi][xi] == world[13][19] or world[yi][xi] == world[13][20] or world[yi][xi] == world[13][
                21] or world[yi][xi] == world[13][22] or world[yi][xi] == world[13][23] or world[yi][xi] == world[13][
                24] or world[yi][xi] == world[13][25]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas pasto - parte 2
            elif world[yi][xi] == world[13][29] or world[yi][xi] == world[13][30]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas agua
            elif world[yi][xi] == world[13][26] or world[yi][xi] == world[13][27] or world[yi][xi] == world[13][28] or \
                    world[yi][xi] == world[14][26] or world[yi][xi] == world[14][27] or world[yi][xi] == world[14][
                28] or world[yi][xi] == world[15][25] or world[yi][xi] == world[15][27] or world[yi][xi] == world[15][
                28] or world[yi][xi] == world[16][26] or world[yi][xi] == world[16][27] or world[yi][xi] == world[16][
                28] or world[yi][xi] == world[17][26] or world[yi][xi] == world[17][27] or world[yi][xi] == world[17][
                28]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas sol
            elif world[yi][xi] == world[1][28] or world[yi][xi] == world[1][29] or world[yi][xi] == world[1][30] or \
                    world[yi][xi] == world[2][27] or world[yi][xi] == world[2][28] or world[yi][xi] == world[2][29] or \
                    world[yi][xi] == world[2][30] or world[yi][xi] == world[3][28] or world[yi][xi] == world[3][29] or \
                    world[yi][xi] == world[3][30] or world[yi][xi] == world[4][27] or world[yi][xi] == world[4][29]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas bloque de tierra - primera fila 1 - parte 1
            elif world[yi][xi] == world[14][1] or world[yi][xi] == world[14][2] or world[yi][xi] == world[14][3] or \
                    world[yi][xi] == world[14][4]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 1 - parte 2
            elif world[yi][xi] == world[14][6] or world[yi][xi] == world[14][7] or world[yi][xi] == world[14][8] or \
                    world[yi][xi] == world[14][9] or world[yi][xi] == world[14][10] or world[yi][xi] == world[14][11] or \
                    world[yi][xi] == world[14][12] or world[yi][xi] == world[14][13] or world[yi][xi] == world[14][
                14] or world[yi][xi] == world[14][15] or world[yi][xi] == world[14][16] or world[yi][xi] == world[14][
                17] or world[yi][xi] == world[14][18] or world[yi][xi] == world[14][19] or world[yi][xi] == world[14][
                20] or world[yi][xi] == world[14][21] or world[yi][xi] == world[14][22] or world[yi][xi] == world[14][
                23] or world[yi][xi] == world[14][24] or world[yi][xi] == world[14][25]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 1 - parte 3
            elif world[yi][xi] == world[14][29] or world[yi][xi] == world[14][30]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas bloque de tierra - primera fila 2 - parte 1
            elif world[yi][xi] == world[15][1] or world[yi][xi] == world[15][2] or world[yi][xi] == world[15][3] or \
                    world[yi][xi] == world[15][4] or world[yi][xi] == world[15][5] or world[yi][xi] == world[15][6] or \
                    world[yi][xi] == world[15][7] or world[yi][xi] == world[15][8] or world[yi][xi] == world[15][9] or \
                    world[yi][xi] == world[15][10] or world[yi][xi] == world[15][11] or world[yi][xi] == world[15][
                12] or world[yi][xi] == world[15][13] or world[yi][xi] == world[15][14] or world[yi][xi] == world[15][
                15] or world[yi][xi] == world[15][16] or world[yi][xi] == world[15][17] or world[yi][xi] == world[15][
                18] or world[yi][xi] == world[15][19] or world[yi][xi] == world[15][20] or world[yi][xi] == world[15][
                21] or world[yi][xi] == world[15][22]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 2 - parte 2
            elif world[yi][xi] == world[15][24]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 2 - parte 3
            elif world[yi][xi] == world[15][29] or world[yi][xi] == world[15][30]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas bloque de tierra - primera fila 3 - parte 1
            elif world[yi][xi] == world[16][1] or world[yi][xi] == world[16][2] or world[yi][xi] == world[16][3] or \
                    world[yi][xi] == world[16][4] or world[yi][xi] == world[16][5] or world[yi][xi] == world[16][6]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 3 - parte 2
            elif world[yi][xi] == world[16][8] or world[yi][xi] == world[16][9]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 3 - parte 3
            elif world[yi][xi] == world[16][11] or world[yi][xi] == world[16][12] or world[yi][xi] == world[16][13] or \
                    world[yi][xi] == world[16][14] or world[yi][xi] == world[16][15] or world[yi][xi] == world[16][
                16] or world[yi][xi] == world[16][17] or world[yi][xi] == world[16][18] or world[yi][xi] == world[16][
                19] or world[yi][xi] == world[16][20] or world[yi][xi] == world[16][21] or world[yi][xi] == world[16][
                22]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 3 - parte 4
            elif world[yi][xi] == world[16][24] or world[yi][xi] == world[16][25]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 3 - parte 5
            elif world[yi][xi] == world[16][29] or world[yi][xi] == world[16][30]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas bloque de tierra - primera fila 4 - parte 1
            elif world[yi][xi] == world[17][1]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 4 - parte 2
            elif world[yi][xi] == world[17][3] or world[yi][xi] == world[17][4] or world[yi][xi] == world[17][5] or \
                    world[yi][xi] == world[17][6] or world[yi][xi] == world[17][7] or world[yi][xi] == world[17][8] or \
                    world[yi][xi] == world[17][9] or world[yi][xi] == world[17][10] or world[yi][xi] == world[17][11] or \
                    world[yi][xi] == world[17][12] or world[yi][xi] == world[17][13] or world[yi][xi] == world[17][
                14] or world[yi][xi] == world[17][15] or world[yi][xi] == world[17][16] or world[yi][xi] == world[17][
                17] or world[yi][xi] == world[17][18] or world[yi][xi] == world[17][19] or world[yi][xi] == world[17][
                20] or world[yi][xi] == world[17][21] or world[yi][xi] == world[17][22]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 4 - parte 3
            elif world[yi][xi] == world[17][24] or world[yi][xi] == world[17][25]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 4 - parte 5
            elif world[yi][xi] == world[17][29] or world[yi][xi] == world[17][30]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas bloque de tierra - primera fila 5 - parte 1
            elif world[yi][xi] == world[18][1] or world[yi][xi] == world[18][2] or world[yi][xi] == world[18][3] or \
                    world[yi][xi] == world[18][4]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 5 - parte 2
            elif world[yi][xi] == world[18][6] or world[yi][xi] == world[18][7] or world[yi][xi] == world[18][8] or \
                    world[yi][xi] == world[18][9] or world[yi][xi] == world[18][10] or world[yi][xi] == world[18][11] or \
                    world[yi][xi] == world[18][12] or world[yi][xi] == world[18][13] or world[yi][xi] == world[18][
                14] or world[yi][xi] == world[18][15] or world[yi][xi] == world[18][16] or world[yi][xi] == world[18][
                17] or world[yi][xi] == world[18][18] or world[yi][xi] == world[18][19] or world[yi][xi] == world[18][
                20] or world[yi][xi] == world[18][21] or world[yi][xi] == world[18][22]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 5 - parte 3
            elif world[yi][xi] == world[18][24] or world[yi][xi] == world[18][25] or world[yi][xi] == world[18][26] or \
                    world[yi][xi] == world[18][27] or world[yi][xi] == world[18][28] or world[yi][xi] == world[18][
                29] or world[yi][xi] == world[18][30]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas bloque de tierra - primera fila 6 - parte 1
            elif world[yi][xi] == world[19][1] or world[yi][xi] == world[19][2] or world[yi][xi] == world[19][3] or \
                    world[yi][xi] == world[19][4] or world[yi][xi] == world[19][5] or world[yi][xi] == world[19][6]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 6 - parte 2
            elif world[yi][xi] == world[19][8] or world[yi][xi] == world[19][9] or world[yi][xi] == world[19][10] or \
                    world[yi][xi] == world[19][11] or world[yi][xi] == world[19][12] or world[yi][xi] == world[19][
                13] or world[yi][xi] == world[19][14]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 6 - parte 3
            elif world[yi][xi] == world[19][16] or world[yi][xi] == world[19][17] or world[yi][xi] == world[19][18] or \
                    world[yi][xi] == world[19][19] or world[yi][xi] == world[19][20] or world[yi][xi] == world[19][
                21] or world[yi][xi] == world[19][22] or world[yi][xi] == world[19][23] or world[yi][xi] == world[19][
                24] or world[yi][xi] == world[19][25] or world[yi][xi] == world[19][26] or world[yi][xi] == world[19][
                27] or world[yi][xi] == world[19][28]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
            # coordenadas bloque de tierra - primera fila 6 - parte 4
            elif world[yi][xi] == world[19][30]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '

            # coordenadas bloque de tierra - primera fila 7
            elif world[yi][xi] == world[20][1] or world[yi][xi] == world[20][2] or world[yi][xi] == world[20][3] or \
                    world[yi][xi] == world[20][4] or world[yi][xi] == world[20][5] or world[yi][xi] == world[20][6] or \
                    world[yi][xi] == world[20][7] or world[yi][xi] == world[20][8] or world[yi][xi] == world[20][9] or \
                    world[yi][xi] == world[20][10] or world[yi][xi] == world[20][11] or world[yi][xi] == world[20][
                12] or world[yi][xi] == world[20][13] or world[yi][xi] == world[20][14] or world[yi][xi] == world[20][
                15] or world[yi][xi] == world[20][16] or world[yi][xi] == world[20][17] or world[yi][xi] == world[20][
                18] or world[yi][xi] == world[20][19] or world[yi][xi] == world[20][20] or world[yi][xi] == world[20][
                21] or world[yi][xi] == world[20][22] or world[yi][xi] == world[20][23] or world[yi][xi] == world[20][
                24] or world[yi][xi] == world[20][25] or world[yi][xi] == world[20][26] or world[yi][xi] == world[20][
                27] or world[yi][xi] == world[20][28] or world[yi][xi] == world[20][29] or world[yi][xi] == world[20][
                30]:
                world[yi][xi] = Back.LIGHTWHITE_EX + '    '
