from time import sleep

lista = []
while True:
    cliente = input('Digite o nome do cliente: ')
    lista.append(cliente)
    while True:
        resp = input('continua? [S/N]: ')
        if resp in 'sn':
            break
    if resp =='n':
        break


while lista:
    atendido = lista.pop(0)
    print(f'Atendido: {atendido}')
    sleep(1)
    print(f'A seguir: {lista}')      
    sleep(1)

#print(f'Fila atual: {lista}')
#atendido = lista.pop(0)
#print(f'Atendido: {atendido}')
#print(f'Fila depois do atendimento: {lista}')
