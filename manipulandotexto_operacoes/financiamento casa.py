valorcasa = int(input('Digite o valor da casa a ser comprada: ')) 
sal = int(input('Digite o seu salario atual: '))
anos = int(input('Digite a quantidade de anos em que será realizado o financiamento: '))

meses = anos * 12
prest = valorcasa // meses
teto = sal * 0.30
if prest >= teto:
    print (f"""Infelizmente não podemos aprovar o crédito do financiamento. O valor da parcela de {prest} ultrapassará 30% de sua renda! 
O seu limite para pagamento mensal é de {teto}!""")
elif prest < teto:
    print(f'O crédito para o financiamento foi aprovado! O valor da parcela ficará em {prest} reais mensais por {meses} meses!')