import main as n
wood = 0
rock = 0
option = input('$ ')
if option == 'init':
    while True:
        option = input('$ ')
        print('$ Welcome to minecraft world XYZ')
        n.move_player(option)
        if "extract" in option:
            n.collect(option)
            wood = wood + n.collect(option)[1]
            rock = rock + n.collect(option)[0]
        print("Wood blocks:", wood)
        print("Stone blocks:", rock)
        if option=="exit":
            break
        intento = 1
