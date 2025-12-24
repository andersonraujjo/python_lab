from time import sleep

lista = [{'nome':'João','idade':27},{'nome':'Leila','idade':45},{'nome':'Laura','idade':28}]
dicion = {}



def tabela(tabela):
    print('\033[92mPESSOAS CADASTRADAS\033[0m')
    print('\n')
    for i in lista:
        print(f'Nome: {i['nome']:<25} Idade: {i['idade']:>3}')
    return tabela


while True:
    print('-'*30)
    print('\033[1mMENU PRINCIPAL\033[0m')
    print("""Escolha uma opção:
      1 - Ver pessoas cadastradas
      2 - Cadastrar nova pessoa
      3 - Sair do sistema""")
    print('-'*30)

    resposta = input('>>>')

    if resposta == '3':
        break

    elif resposta == '1':
        tabela(lista)

    elif resposta == '2':
        print('\033[92mNOVO CADASTRO\033[0m')
        dicion['nome'] = input('Digite o nome da pessoa: ')
        
        while True:
            dicion['idade'] = input('Digite a idade: ')
            if dicion['idade'].isnumeric():
                break
            else:
                print('\033[91mPor favor, digite um número válido.\033[0m')
        print(f'\033[92mRegistro de {dicion['nome']} adicionado com sucesso.\033[0m')
        
        lista.append(dicion.copy())
        dicion.clear()
    else:
        print('\033[91mErro. Por favor digite uma opção válida.\033[0m')

        
print('\033[1m\033[94mSaindo do sistema...')
sleep(1.5)        
print('ATÉ LOGO!')