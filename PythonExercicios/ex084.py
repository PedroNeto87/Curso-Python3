temp = list()
principal = list()
maior = menor = qtd = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp [1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    continuar = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    qtd += 1
    if continuar == 'N':
        break
print(f'Ao todo, você cadastrou {qtd} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}')
