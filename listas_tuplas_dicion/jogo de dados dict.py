



from random import randint
from time import sleep
from operator import itemgetter


dados = {}

for i in range (1,5):
    dados[f'Jogador {i}'] = randint(1,6)

for k,v in dados.items():
    print(f'O jogador {k} tirou {v}')   
    sleep(1) 

ranking = []
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)    
print('-'*30)
for k, v in enumerate(ranking):
    print(f'{k+1}° Lugar: {v[0]} tirou {v[1]}')
    sleep(1)




    
    

