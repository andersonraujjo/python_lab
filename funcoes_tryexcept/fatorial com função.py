


def fatorial (a,show=False):
    """
    Calcula o fatorial de um número e, opcionalmente, mostra o cálculo.
    :para a: O número a ser calculado.
    :para show: (Opcional) Mostra ou não o cálculo. Padrão é False.
    :return: O valor do fatorial de a.
    """
    f = 1
    for i in range(a,0,-1):
        f = f * i
        if show==True:
            print(i,end=' ')
            if i > 1:
                print('X', end=' ')
            else:
                print('= ',end='')
    return f

print(fatorial(5, show=True)) 
