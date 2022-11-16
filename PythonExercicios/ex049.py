print('==TABUADA==')
n1 = int(input("Digite um número para que seja calculado em nossa tabuada: "))
print('=' * 12)
for c in range(11):
    print('{} X {:2} = {}'.format(n1, c, n1*c))
print('=' * 12)
