
def draw_worldempty ():
    import colorama
    import colorama as init
    from colorama import Back, Style,Fore
    import numpy as np
    colorama.init(autoreset=True)
    world = [[Back.WHITE + '' for  j in range(31)]for i in range(21)]
    world = np.array(world)

    world[0] = [i for i in range(31)]

    print('\n'.join([''.join(['{:4}'.format(columna) for columna in fila])
                     for fila in world]))




draw_worldempty()
