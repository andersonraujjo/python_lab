

termo = int(input('Digite o primeiro termo: '))

r = int(input('Digite a razão da PA: '))
lim = termo + (10 - 1) * r

for i in range (termo, lim+r, r):
    print(i)
