from math import*
from time import sleep
import os



def corpo_1():
    x = 0
    while x<1:
        
        et = input('\ndigite aqui: ')

        if et == 'sair':
            print('A essa calculadora será fechada!')
            sleep(3)
            x = 2
            break
        else:
            im = int(et)

            out = isqrt(im)
            print(f'input: {im}\t output: {out}\n')

corpo_1()
os.system("cls")
import CENTRAL
quit('cal1.py')