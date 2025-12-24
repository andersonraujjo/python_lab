



palavras_tupla = ('lua', 'rojao', 'pinheiro', 'sol', 'travesseiro', 'apagador', 'mel', 'viagem', 'telefone')



for i in palavras_tupla:
        capsloca = i.upper()
        print(f'Na palavra {capsloca} tem as vogais', end=' ')
        palavra_isolada = str(i)
        for letra in palavra_isolada:
                if letra in 'aeiou':
                        print(letra, end=' ')
        print('\n')


