




def notas(*num,sit=False):
    """
    O *num aponta que a função receberá vários numeros, o sit=False, por padrão, desativa a funcionalidade.
    Se caso True, ela executa a segunda parte da função retornado  a situação do aluno.
    Importante lembrar que o que está dentro de notas(algo) irá lá pra cima, no def da função (notas(*num) por exemplo)
    """
    dicion = {}
    dicion['total'] = len(num)
    dicion['maior'] = max(num)
    dicion['menor'] = min(num)
    dicion['media'] = sum(num) / len(num)
    if sit==True:  
        if dicion['media'] >= 7:
            dicion['situação'] = 'Aprovado'
        elif dicion['media'] <= 5:
            dicion['situação'] = 'Ruim'
        elif dicion['media'] > 5 and dicion['media'] < 6:
            dicion['situação'] = 'Razoavel'
        else:
            dicion['situação'] = 'Boa'
    return dicion

resp = notas(5,9,8,7,9,2,1,sit=True)
print(resp)
help(notas)