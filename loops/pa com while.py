

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão da pa: '))


pa = termo + razao
contador = 2
lista = [termo,pa]

while contador <10:
    contador = contador + 1
    pa = pa + razao
    lista.append(pa)

print(lista)
