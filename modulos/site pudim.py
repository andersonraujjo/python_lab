

import requests


url = "https://www.pudim.com.br/"

try:
    resposta = requests.get(url)

    if resposta.status_code == 200:
        #codigo 200 é o codigo de acesso bem sucedido
        print('Consegui acessar o site Pudim!')
        #print(resposta.text)

    else:
        print(f'Não consegui acessar o site Pudim. Erro {resposta.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Ocorreu o erro {e}.')