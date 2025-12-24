

print('\n')
times = ("Flamengo", "Cruzeiro", "Bragantino", "Palmeiras", "Bahia", "Fluminense", "Atlético-MG", "Botafogo", "Mirassol", "Corinthians", "Grêmio", "Chapecoense", "Vasco da Gama", "São Paulo", "Santos", "EC Vitória", "Internacional", "Fortaleza", "Juventude", "Sport Recife")

print(f'Os 5 primeiros colocados são {times[0:5]}')
print('_'*100, '\n')

print(f'Os ultimos 4 colocados da tabela são {times[-4:]}')
print('_'*100, '\n')

print('Os times em ordem alfabética:')
print(sorted(times))

print('_'*100, '\n')
posicao_chapeco = times.index('Chapecoense') + 1
print(f'O time da Chapecoense se encontra na {posicao_chapeco}° posição.')
print('_'*100, '\n')


