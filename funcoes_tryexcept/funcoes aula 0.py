def separador():
    print('/'*30)
separador()

def soma (a,b):
    s = a + b
    print(s)

soma(5,8)
soma(2,9)
soma(13,22)

separador()

def mensagem(msg):
    print('---------------------------------------')
    print(msg)
    print('---------------------------------------')
mensagem('CADASTRO DE ALUNOS')
separador()

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

titulo('Curso em video')
titulo('Python')
titulo('Guanabara')
separador()
def contador(*num):
    print(num)

contador(1,2,3,4)
contador(4,5,6)
contador(9,8,7)