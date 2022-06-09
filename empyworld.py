
def draw_worldempty ():
    import colorama
    import colorama as init
    from colorama import Back, Style, Fore
    colorama.init()
    world = [[j for  j in range(20)]for i in range(30)]
    for i in range(len(world)):
        print([Back.GREEN for j in range(len(world[i]))])





draw_worldempty()