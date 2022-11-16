lista = 'Lápis', 1.50, 'Borracha', 0.75, 'Caneta', 2.50, 'Corretivo', 3, 'Caderno', 25, 'Régua', 2.75, 'Mochila', 89.90, 'Fichario', 59.90
soma = 0
print('-'*40)
print(f'\033[1m{"LISTAGEM DE PREÇOS":^40}\033[m')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
        soma += lista[pos]
print('-'*40)
print('\033[1mTOTAL\033[m', end='')
print(f'{"R$":.>27}', end=' ')
print(f'{soma:.2f}')
