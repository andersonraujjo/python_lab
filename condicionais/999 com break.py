


soma = 0
cont = 0

while True:
    num = int(input('Digite um número [999 sai do programa]: '))
    if num == 999:
        break
    soma = num + soma
    cont += 1
   

print(f'A soma de todos os {cont} numeros digitados foi de {soma}!')
