'''temp = []
par = []
impar = []
for c in range(1,8):
    temp.append(int(input(f'Digite o {c}º valor: ')))
for i, v in enumerate(temp):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores impares digitados foram: {sorted(impar)}')'''
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Insira o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
print(f'{num}')
