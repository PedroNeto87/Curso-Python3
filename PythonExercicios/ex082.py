a = []
pares = []
impares = []
while True:
    a.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for i, v in enumerate(a):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {a}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
