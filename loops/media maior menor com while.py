


lista = []

 
while True:
   num =  int(input('Digite um numero: '))
   continuar = int(input('Deseja continuar? [1] para sim [2] para não: '))
   lista.append(num)

   
   if continuar != 1 and continuar !=2:
      print('opção invalida')
   
   if continuar == 2:
      break

qtdelista = len(lista)
soma = sum(lista)
media = soma / qtdelista

print(f'a média entre os {qtdelista} numeros foi de {media}')
print(f'o maior valor é o {max(lista)} e o menor é o {min(lista)}')