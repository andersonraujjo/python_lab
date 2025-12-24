
vermei = '\033[91m'

def msgg():
    
    msg = 'SISTEMA DE AJUDA PYHELP'
    print('\033[94m','-'*len(msg))
    print(msg)
    print('-'*len(msg))
    


def ajuda(resposta):
    help(resposta)
    return help

while True:
    msgg()
    resposta_usuario = input('\033[92m''Digite a função ou biblioteca para a busca: ').lower()
    if resposta_usuario == 'fim':
        break
    print()
    print(f'{vermei}Ajuda da função {resposta_usuario}:')
    
    ajuda(resposta_usuario)