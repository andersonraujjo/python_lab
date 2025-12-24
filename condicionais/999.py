


num = 0
lista = []
cont = 0

while num !=999:
    cont = cont + 1
    num = int(input('Digite um numero inteiro (999 interrompe o programa): '))
    lista.append(num)

soma = sum(lista)
total = soma - 999

print(f'Foram digitados {cont} numeros inteiros e a soma deles é o total de {total}!')