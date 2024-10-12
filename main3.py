from colorama import Back, init

init(autoreset=True)
world = [[Back.LIGHTWHITE_EX + '    ' for i in range(42)] for j in range(21)]  # matriz por comprension, representa
# 20x 30 y ponemos 32 para poner los numeros y 31- 1 y 21-1 nos da 30 y
# 20, 30 x 20
world2 = [[Back.LIGHTWHITE_EX + '    ' for i in range(42)] for j in range(21)]  # matriz por comprension, representa

ESPACIONEGRO = Back.BLACK + '    '  # variables que usaremos mas tarde para determinar un pixel negro, azul y verde
PASTO = Back.GREEN + '    '
AGUA = Back.BLUE + '    '
SOL = Back.YELLOW + '    '

def draw_worldempty():
    for i in range(len(world)):  # recorremos las filas de la matriz con len
        if i == 0:
            for j in range(len(world[i])):  # selecciona todos los elementos de esas fila
                world[i][j] = str(j)  # cada uno se convierte en un string
        for l in range(42):  # seleccionar a los primeros valores de cada fila, si l es 0 entonces vemos que es la
            # primera
            if l == 0:
                world[i][l] = str(i)  # i representa a todas las filas y l representa al primer elementos de cada
                # fila y entonces seleccionamos a todos los primeros elementos de cada fila para convertirlos

def paint():
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
    #
    world[7][37] = Back.RED + '    '
    world[8][37] = Back.RED + '    '
    world[9][37] = Back.RED + '    '
    world[10][37] = Back.RED + '    '
    world[11][37] = Back.RED + '    '
    world[12][37] = Back.RED + '    '
    world[6][34] = Back.GREEN + '    '
    world[6][35] = Back.GREEN + '    '
    world[6][36] = Back.GREEN + '    '
    world[6][37] = Back.GREEN + '    '
    world[6][38] = Back.GREEN + '    '
    world[6][39] = Back.GREEN + '    '
    world[6][40] = Back.GREEN + '    '
    world[5][35] = Back.GREEN + '    '
    world[5][36] = Back.GREEN + '    '
    world[5][37] = Back.GREEN + '    '
    world[5][38] = Back.GREEN + '    '
    world[5][39] = Back.GREEN + '    '
    world[4][36] = Back.GREEN + '    '
    world[4][37] = Back.GREEN + '    '
    world[4][38] = Back.GREEN + '    '
    world[3][37] = Back.GREEN + '    '

    #
    world[10][39] = Back.RED + '    '
    world[11][39] = Back.RED + '    '
    world[12][39] = Back.RED + '    '
    world[9][38] = Back.GREEN + '    '
    world[9][39] = Back.GREEN + '    '
    world[9][40] = Back.GREEN + '    '
    world[8][39] = Back.GREEN + '    '

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
    world[16][34] = Back.WHITE + '    '
    world[12][35] = Back.WHITE + '    '
    world[16][37] = Back.WHITE + '    '
    world[18][37] = Back.WHITE + '    '
    world[18][40] = Back.WHITE + '    '

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
    world[2][31] = Back.LIGHTYELLOW_EX + '    '
    world[4][31] = Back.LIGHTYELLOW_EX + '    '
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

def draw_world():  # seleccionamos las filas que queremos pintar y el numero de columnas que pintaremos, y cambiamos
    # los pixeles balncos según el color que corresponda
    # La parte negra
    for i in range(14, 21):
        for j in range(40):
            world[i][j + 1] = ESPACIONEGRO  # j + 1 es para evitar que se pinten los numeros
    # la parte verde
    for i in range(13, 14):
        for j in range(40):
            world[i][j + 1] = PASTO

        # La parte de agua
        for i in range(13, 18):
            for j in range(25, 28):
                world[i][j + 1] = AGUA
    paint()



def draw_world2empty():
    for i in range(len(world2)):  # recorremos las filas de la matriz con len
        if i == 0:
            for j in range(len(world2[i])):  # selecciona todos los elementos de esas fila
                world2[i][j] = str(j)  # cada uno se convierte en un string
        for l in range(42):  # seleccionar a los primeros valores de cada fila, si l es 0 entonces vemos que es la
            # primera
            if l == 0:
                world2[i][l] = str(i)  # i representa a todas las filas y l representa al primer elementos de cada
                # fila y entonces
                # seleccionamos a todos los primeros elementos de cada fila para convertirlos


def draw_world2():  # seleccionamos las filas que queremos pintar y el numero de columnas que pintaremos, y cambiamos
    # los pixeles balncos según el color que corresponda
    # La parte negra
    for i in range(14, 21):
        for j in range(40):
            world2[i][j + 1] = ESPACIONEGRO  # j + 1 es para evitar que se pinten los numeros
    # la parte verde
    for i in range(13, 14):
        for j in range(40):
            world2[i][j + 1] = PASTO
        # La parte de agua
        for i in range(13, 18):
            for j in range(25, 28):
                world2[i][j + 1] = AGUA
    paint()



def draw_player(yi, xi):  # Mismo proceso que el anterior para dibujar al avatar
    # Avatar
    world[yi][xi] = Back.MAGENTA + '    '  # la mano
    world[yi][xi - 1] = Back.CYAN + '    '  # centro
    world[yi - 1][xi - 1] = Back.CYAN + '    '  # pies
    world[yi + 1][xi - 1] = Back.CYAN + '    '  # cabeza

def fill(yi, xi):  #esta funcion compara el mundo uno con el mundo dos
    world[yi][xi] = world2[yi][xi]
    world[yi][xi - 1] = world2[yi][xi - 1]
    world[yi - 1][xi - 1] = world2[yi - 1][xi - 1]
    world[yi + 1][xi - 1] = world2[yi + 1][xi - 1]
#si esta funcion detecta que si al comparar el mundo 1 esta de color rojo, pinta de color blanco al mundo 2


def arbol(yi, xi): # llamar a la variable global
    global world2 #llamamos al segundo mundo para que el primer mundo no se dibuje y se borre el color
    if world2[yi][xi] == Back.RED + '    ': #si detecta un color rojo lo cambia
        return True
    return False


def piedra(yi, xi): # usamos el mismo paso anterior, llamamos a la variable global
    global world2 #llamamos al segundo mundo para que el primer mundo no se dibuje y se borre el color
    if world2[yi][xi] == Back.WHITE + '    ':
        return True
    return False


def destroy(yi, xi): #funcion que usamos para destruir
    world[yi][xi] = Back.LIGHTWHITE_EX + '    ' #pinta de blanco lo que destruyamos en nuestro mundo 1
    world2[yi][xi] = Back.LIGHTWHITE_EX + '    ' #pinta de blanco lo que destruyamos en nuestro mundo 2


def collect(yi, xi):
    countwood = 0  # inicia la cuenta en 0
    countrock = 0
    # indicadores de la mano del jugador
    # recibe el zx y el zy para que collect se ejecute siempre en el espacio
    # de la mano del jugador sin importar el numero de comandos

    # Verifica que la mano del jugador se encuentra en el mismo espacio que un arbol
    if arbol(yi, xi):
        countwood += 1
    # Verifica que la mano del jugador se encuentra en el mismo espacio que una piedra
    if piedra(yi, xi):
        countrock += 1
    # Retorna el contador de los bloques destruidos
    destroy(yi, xi)
    return countwood, countrock


def build(yi, xi, elemento): #esta funcion sirve para construir
    if world2[yi][xi] == Back.LIGHTWHITE_EX + '    ' and elemento == 'wood': #construir bloques de madera en ambos mundos
        world[yi][xi] = Back.RED + '    ' #bloques de madera color rojo en el mundo
        world2[yi][xi] = Back.RED + '    ' #bloques de madera color rojo en el mundo 2
    elif world2[yi][xi] == Back.LIGHTWHITE_EX + '    ' and elemento == 'rock':
        world[yi][xi] = Back.RED + '    ' #bloques de piedra color rojo en el mundo
        world2[yi][xi] = Back.RED + '    ' #bloques de piedra color rojo en el mundo 2
    else:
        print('Invalid operation') #por si la funcion no cumple con los requerimentos

def print_map(wood, rock, xi, yi, camara, limite):
    if xi in range(1, 41) and yi in range(1, 21):  # Check if the player is within the world
        draw_player(yi, xi)
        print('$ Welcome to Minecraft world XYZ')
        for y in range(21):  # Print the matrix
            for x in range(len(world[y])):
                if limite + camara - 30 <= x <= limite + camara:  # Last column to print
                    print(world[y][x].center(4), end='')  # Print the matrix
                elif x == limite + 1 + camara:  # Print a new line for the next row
                    print()
                    break
        print("Wood blocks:", wood)
        print("Stone blocks:", rock)


def move_player2(wood, rock):  # Recibe los valores en el modulo para guardar la cuenta de collect
    xi = 3
    yi = 11
    camara = 0 # lo que se suma o resta a nuestros movimientos
    limite = 30
    # hacemos un bucle para jugar el tiempo deseado
    while True:

        moves = input('$ ').split(',')  # aqui recibe los comandos en una string y se convierte el string en una lista para manejarla
        # aqui se cambian las coordenadas de los pixeles del cuerpo del jugador para poder moverlo despues
        for i in range(len(moves)):
            moves[i] = moves[i].split(' ')

        for i in moves:
             ogx1 = xi
             ogy1 = yi
             ogwood = wood
             ogrock = rock

             if len(i) > 1 and i[1] == 'right':
                    # es necesario para que el jugador no tenga un clon
                    fill(yi, xi)
                    xi += int(i[0])
                    #intentamos asegurar de que el jugador no se vaya a una parte que no existe
                    modificador = int(i[0]) #comprueba que la modificacion no se salga de los limites
                    if modificador >= 18: #distancia entre 22 a 40
                      modificador -=18
                    if xi >= 23: #cuando el medio del jugador esta en 23
                        camara += modificador
                        if 18 >= camara:
                            while camara >= 18:
                                camara -= 1

             elif len(i) > 1 and i[1] == 'left':
                    fill(yi, xi) # es necesario para que el jugador no tenga un clon
                    xi -= int(i[0])
                    modificador= int(i[0])
                    if modificador >= 18:
                      modificador -=18
                    if xi <= 18:
                        camara -= modificador
                        if 18 >= camara:

                          while camara >= 18:
                              camara-=1

             elif len(i) > 1 and  i[1] == 'down':
                    fill(yi, xi) # es necesario para que el jugador no tenga un clon
                    yi += int(i[0])

             elif len(i) > 1 and i[1] == 'top':
                    fill(yi, xi) # es necesario para que el jugador no tenga un clon
                    yi -= int(i[0])

             if "extract" in i:  # se llama a la funcion colect se si se ingreso el comando extract
                ex = collect(yi, xi)
                wood += ex[0]
                rock += ex[1]  # guarda la cuenta de cada bucle
             if "destroy" in i:  # se llama a la funcion destroy se si se ingreso el comando destroy
                destroy(yi, xi)
            #build wood es parte de la matriz de movimientos al igyal que build rock
             if ['build', 'wood'] in moves and wood > 0:
                w = 'wood'
                build(yi, xi, w)
                wood -= 1
             elif ['build', 'rock'] in moves and rock > 0:
                r = 'rock'
                build(yi, xi, r)
                rock -= 1
             elif ['build', 'wood'] in moves and wood <= 0:
                print('invalid operation')
                print_map(ogwood, ogrock, ogx1, ogy1, camara, limite)

             elif ['build', 'rock'] in moves and rock <= 0:
                print('invalid operation')
                print_map(ogwood, ogrock, ogx1, ogy1, camara, limite)

             if limite + camara > 40: #teniendo en cuenta que 30 es la cantidad de espacios que tendra la pantalla
                while limite + camara > 40:
                    limite -=1
             if camara < 0:
                camara = 0
             if xi in range(1, 41) and yi in range(1, 21):  # se verifica que el jugador este dentro del mundo
                print_map(wood, rock, xi, yi, camara, limite)
                limite = 30
             else:
                print("Invalid operation out of bounds")  # si el jugador se sale del mundo sale operacion invalida
                print_map(ogwood, ogrock, ogx1, ogy1, camara, limite)
