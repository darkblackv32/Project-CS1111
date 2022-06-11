from colorama import Back, Fore, Style, init

init(autoreset=True)


def draw_world_empty():

    for i in range(0, 22):
        print('')                                           #     world = [[Back.LIGHTWHITE_EX + '' for j in range(0, 32)]for i in range(0, 22)]

        for j in range(0, 32):
            if j == 0:
                print('')
            print(Back.LIGHTWHITE_EX + '   ', end = '')


draw_world_empty()