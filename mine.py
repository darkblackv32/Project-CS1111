from main24 import draw_worldempty,draw_world,move_player2,draw_world2empty,draw_world2


def main():
    draw_worldempty()
    draw_world() # llamamos a las funciones anteriores porque nos serviran pora que se ejecute
    draw_world2empty()
    draw_world2()
    wood = 0
    rock = 0
    
    while True:
        option = input('$ ').strip()#se ingresa el init para iniciar el programa
        if option == 'init':
            break
    move_player2(wood, rock)   #se ejecutan las funciones
    
main()
