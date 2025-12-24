

from time import sleep

def contador(a,b,c):
    if c == 0:
        c = 1
    
    if a < b and c <0:
        c = -c
    
    elif a > b and c > 0:
        c = -c

    if a < b:
        b_ajustado = b +1
    else:
        b_ajustado = b-1
    
    
    for i in range (a,b_ajustado,c):
        print(i,end=' ')
        sleep(0.5)

    
contador(1,10,1)
print()
contador(10,0,-2)
print()

a = int(input('Qual o Inicio: '))
b = int(input('Qual o fim: '))
c = int(input('Qual o passo: '))


    
contador(a,b,c)