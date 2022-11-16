while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('=-=' * 12)
    if n < 0:
        break
    for c in range(11):
        print(f'{n} X {c:2} = {n*c}')
    print('=-=' * 12)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
