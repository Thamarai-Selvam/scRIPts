from random import randint 
from time import sleep
from colorama import Fore, Back, Style


x = randint(1,30)

def draw():
    print("\033c") # reset terminal // similar to clrscr();
    for i in range(1,23):
        v = randint(1,x)
        if i == 1:
            c = '$'
            col = Fore.RED if v > 1 else Fore.YELLOW
        elif v % 4 == 0:
            c = '¢'
            col = Fore.RED if v > 15 else Fore.GREEN
        elif v % 3 == 0:
            c = '^'
            col = Fore.GREEN if v > 15 else Fore.RED
        else: 
            c = '*'
            col = Fore.GREEN if v < 15 else Fore.RED
        print(col + Back.WHITE + '{:^33}'.format(c*i))
    print(Style.DIM + Fore.RED + '{:^33}'.format(' || '))
    print('{:^33}'.format(' || '))
    print('{:^33}'.format(' || '))

    sleep(.50)

while True:
    draw()
