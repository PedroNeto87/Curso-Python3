total18 = totalh = totalm = 0
while True:
    print('-' * 20)
    print(' CADASTRE UM PESSOA')
    print('-' * 20)
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo:[M/F] ')).upper().strip()[0]
    if i >= 18:
        total18 += 1
    if s == 'M':
        totalh += 1
    if s == 'F' and i < 20:
        totalm += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {total18}
Ao todo temos {totalh} homens cadastrados
E temos {totalm} mulheres com menos de 20 anos''')
