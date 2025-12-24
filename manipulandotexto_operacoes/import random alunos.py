import random

print ('##################################################')
print ('\n')
print('Vamos sortear um aluno entre 04 para ir apagar a lousa!')

print ('\n')

n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')


aluno = (random.randint(1,4))
if aluno ==1:
    print(f'O aluno escolhido é o/a {n1}')
elif aluno ==2:
    print(f'O aluno escolhido é o/a {n2}')
elif aluno ==3:
    print(f'O aluno escolhido é o/a {n3}')
else:
    print (f'O aluno escolhido é o {n4}')
