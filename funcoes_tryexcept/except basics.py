
try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite o segundo numero: '))
    r = a / b
except (ValueError, TypeError):
    print('Erro relacionado ao tipo de dado digitado.')
except ZeroDivisionError:
    print('O valor não pode ser divido por 0.')
except KeyboardInterrupt:
    print('O usuario optou por não digitar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}.')
else:
    print(f'A divisão de {a} por {b} é igual a {r:.1f}!')
finally:
    print('Mensagem final, independente das anteriores.')
