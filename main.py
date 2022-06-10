from dataclasses import replace

from colorama import Fore,Back,Style
def lines(S, O, L,E):
    for x in range(30):
        if x == S or x == O or x == L or x==E:
            print(Back.YELLOW+ '  ', end="")
            print(Fore.YELLOW + '9', end="")
            continue
        print(Back.LIGHTWHITE_EX + '  ', end="")
        print(Fore.LIGHTWHITE_EX + '0', end="")
    print(Style.RESET_ALL)
lines(27,28,29,-1)
lines(26,27,28,29)
def lines2(D,F,J,W,K,L,E,m,U,c,h,a,v,e,d,i,k,l,s,o,M,B,R,A,N,G,I,p,w,q,z,X,y,f,j,r,):#28
    for x in range(30):
        if x == m or x == U or x == c or x==h or x==a or x==v or x==e or x==d or x==i or x==k or x == W or x == K or x == L or x == E or x == D or x == F or x == J:
            print(Back.GREEN+ '  ', end="")
            print(Fore.GREEN + '4', end="")
            continue
        elif x== l or x==s or x==o:
            print(Back.YELLOW+ '  ', end="")
            print(Fore.YELLOW + '9', end="")
            continue
        elif x==M or x==B or x==R or x==A or x==N or x==G:
            print(Back.RED + '  ', end="")
            print(Fore.RED + '1', end="")
            continue
        elif x==I or x==p or x==w or x==q or x==z or x==X or x==y or x==f:
            print(Back.WHITE + '  ', end="")
            print(Fore.WHITE + '0', end="")
            continue
        elif x==j:
            print(Back.LIGHTBLUE_EX + '  ', end="")
            print(Fore.LIGHTBLUE_EX + '2', end="")
            continue
        elif x==r:
            print(Back.MAGENTA + '  ', end="")
            print(Fore.MAGENTA + '3', end="")
            continue
        print(Back.LIGHTWHITE_EX + '  ', end="")
        print(Fore.LIGHTWHITE_EX + '0', end="")
    print(Style.RESET_ALL)
lines2(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,21,-1,-1,-1,-1,27,28,29,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
lines2(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,20,21,22,-1,-1,-1,26,28,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
lines2(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,19,20,21,22,23,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
lines2(-1,-1,-1,-1,-1,-1,-1,10,16,18,19,20,21,22,23,24,4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
lines2(-1,-1,-1,-1,-1,-1,3,4,5,9,10,-1,15,16,17,11,-1,-1,-1,-1,-1,21,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
lines2(28,24,18,12,8,2,3,4,5,9,10,6,15,16,17,11,14,-1,-1,-1,-1,21,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
lines2(24,25,23,28,29,27,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,16,21,10,4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)
lines2(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,16,21,10,4,24,28,-1,-1,-1,-1,7,-1,-1,-1,1,-1)
lines2(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,16,21,10,4,24,28,-1,-1,-1,6,7,8,15,-1,1,2)
lines2(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,16,21,10,4,24,28,11,29,19,6,7,8,15,14,1,-1)

for i in range(1):
    if i==0 :
        for x in range(25):
            print(Back.GREEN+'  ',end="")
            print(Fore.GREEN + '4', end="")
        for a in range(3):
            print(Back.BLUE+'  ',end="")
            print(Fore.BLUE + '5', end="")
        for x in range(2):
            print(Back.GREEN+'  ',end="")
            print(Fore.GREEN + '4', end="")
        print(Style.RESET_ALL)
    def linea (m,d,e):
        for x in range(25):
            if x==m or x==d or x==e:
                print(Back.WHITE + '  ', end="")
                print(Fore.WHITE + '6', end="")
                continue
            print(Back.BLACK+'  ',end="")
            print(Fore.BLACK + '7', end="")
        for a in range(3):
            print(Back.BLUE+'  ',end="")
            print(Fore.BLUE + '5', end="")
        for x in range(2):
            print(Back.BLACK+'  ',end="")
            print(Fore.BLACK + '7', end="")
        print(Style.RESET_ALL)

linea(4,-1,-1)
linea(22,24,-1)
linea(6,9,22)
linea(1,22,-1)
def linea2(R, E, D):
    for x in range(30):
        if x == R or x == E or x == D:
            print(Back.WHITE + '  ', end="")
            print(Fore.WHITE + '6', end="")
            continue
        print(Back.BLACK + '  ', end="")
        print(Fore.BLACK + '7', end="")
    print(Style.RESET_ALL)
linea2(4,22,-1)
linea2(6,14,28)
linea2(-1,-1,-1)

"0".replace(str(0),str(1))