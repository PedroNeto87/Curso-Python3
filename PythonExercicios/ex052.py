n = int(input('Digite um numero: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(n, total))
if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')
