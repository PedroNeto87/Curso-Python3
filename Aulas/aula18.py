'''galera = [['João', 20], ['Maria', 18], ['Felipe', 30], ['Ana', 39]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''
galera = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
#print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')
