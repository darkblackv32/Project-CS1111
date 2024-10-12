def draw_worldempty ():
    import colorama
    import colorama as init
    from colorama import Back, Style,Fore
    import numpy as np
    colorama.init(autoreset=True)
    world = [[Back.WHITE + '' for  j in range(31)]for i in range(21)]
    world = np.array(world)
    d = -1
    world[0] = [i for i in range(31)]
    for i in range(len(world)):

        d = d + 1
        for j  in range (len(world[i])):

            world[i][0] = d


    print('\n'.join([''.join(['{:4}'.format(columna) for columna in fila])
                     for fila in world]))




draw_worldempty()
