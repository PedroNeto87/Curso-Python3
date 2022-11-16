n = int(input('Primeiro valor: ')), int(input('Segundo valor: ')), int(input('Terceiro valor: ')), int(input('Quarto valor: '))
print(f'Você digitou os valores: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for par in n:
    if par % 2 == 0:
        print(par, end=' ')
