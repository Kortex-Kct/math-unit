from math import*
from time import sleep
import os

def corpo_2():
    x = 0 
    lis = []
            
    n = int(input('quantos temos você quer achar? : '))

    for item in range(5):
        entrada = float(int(input(f'insira: ')))
        lis.append(entrada)
        lis.sort()
        print('\n',lis)

    r = lis[1]/ lis[0]

    a1 = lis[0]
    AN = a1+(n-1)*r
    print(f' o an é {AN}')

corpo_2()