

num = int(input('Digite um numero de 1 a 26: '))

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

if num <= 0 or num >26:
    print('Numero invalido!')
else:
    print(alfabeto[0:num])
