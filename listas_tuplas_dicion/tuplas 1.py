


numeros_por_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    numero_usuario = int(input('Digite um número entre 0 e 20: '))
    if numero_usuario <0 or numero_usuario >20:
        print('Tente novamente!')
    else:
        break

print(f'O número {numero_usuario} escrito por extenso é {numeros_por_extenso[numero_usuario]}!')
