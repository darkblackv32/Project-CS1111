from main3 import draw_worldempty, draw_world, move_player2, draw_world2empty, draw_world2
# se importan las funciones anteriores

def main():
    draw_worldempty() # llamamos a las funciones anteriores porque nos serviran pora que se ejecute
    draw_world()  # llamamos a las funciones anteriores porque nos serviran pora que se ejecute
    draw_world2empty() # llamamos a las funciones anteriores porque nos serviran pora que se ejecute
    draw_world2() # llamamos a las funciones anteriores porque nos serviran pora que se ejecute
    wood = 0 # el valor con el que empieza nuestro contador de madera
    rock = 0 # el valor con el que empieza nuestro contador de piedras

    while True:
        option = input('$ ').strip()  # se ingresa el init para iniciar el programa
        if option == 'init': # si el usuario coloca init, se romperá
            break
    move_player2(wood, rock)  # se ejecutan las funciones

main()
