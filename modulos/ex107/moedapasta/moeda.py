
def dobro(a,b=False):    
    resp =  a * 2
    if b==True:
        return cifrao(resp)
    else:
        return resp
    

def metade(a,b=False):
    resp =  b / 2
    if b==True:
        return cifrao(resp)
    else:
        return resp

def aumentar(a,b=False):
    dez_por_cento = a * 0.10 
    resp = a + dez_por_cento
    if b==True:
        return cifrao(resp)
    else:
        return resp
    

def diminuir(a,b=False):
    treze_por_cento = a * 0.13
    resp = a - treze_por_cento
    if b==True:
        return cifrao(resp)
    else:
        return resp
    
def cifrao(a):
    a_str = str(a)
    a_str_f =  a_str.replace('.', ',')
    a_str_f = 'R$' + a_str_f
    return a_str_f

