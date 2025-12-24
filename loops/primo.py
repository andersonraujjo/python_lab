num = int(input('Digite um numero: '))
conta = 0
for i in range (1,num+1):
    if num % i == 0:
        conta = conta + 1
if conta == 2:
    print('primo')
else:
    print('nop')