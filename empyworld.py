def draw_worldempty ():
    import colorama
    import colorama as init
    from colorama import Back, Style, Fore
    colorama.init(autoreset=True)
    world = [[j for  j in range(20)]for i in range(30)]
    print(i for i in range(30))
    for i in range(len(world)):
        for j in range(len(world[i])):
          print(Back.GREEN + ' ',end='')




draw_worldempty()
