

while True:
    tabuada = int(input('Qual a tabuada? '))
    if tabuada <0:
        break
    for i in range (1,11):
        tab = tabuada * i
        print(f'{tabuada} x {i} = ',tab)

print('PROGRAMA ENCERRADO.')