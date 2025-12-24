


import time
import random

escolha_de_jogos = int(input('Quantos jogos serão sorteados? '))

lista_dos_numeros = []

for v in range(0,escolha_de_jogos):
    lista_dos_numeros.append([])
    
    for i in range (1,7):
        escolha_maquina = random.randint(1,61)
        
        while escolha_maquina in lista_dos_numeros[v]:
            escolha_maquina = random.randint(1,61)
        
        lista_dos_numeros[v].append(escolha_maquina)

for k in range(0, escolha_de_jogos):
    lista_dos_numeros[k].sort()
    
    print(f'Jogo {k+1}: {lista_dos_numeros[k]}')
    time.sleep(1)
        


