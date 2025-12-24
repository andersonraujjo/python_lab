########### Gabarito de provas ##########

print("\n")
print ('Vamos começar inserindo as notas de cada matéria, que o sistema retornará  se o candidato foi aprovado ou não.')
print ("\n")



    
lista_de_materias = ['matematica','portugues','biologia','geografia','historia','ingles','fisica']
            

    
for i in lista_de_materias:   

    nota = input (f'Qual a nota do aluno na matéria {i}? ')
    nota = int (nota)
    if nota >= 6:
        print ('Aprovado!')
    elif nota <=5:
        print ('Reprovado!')





#nota = input ('Qual a nota do aluno na matéria {} ? '.format(i))




