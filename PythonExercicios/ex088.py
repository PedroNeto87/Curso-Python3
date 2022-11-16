from time import sleep
from random import randint
lista = []
jogos = []
print('-' * 43)
print(f'{"PALPITES MEGA SENA":^43}')
print('-' * 43)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 6, f'SORTEANDO {qtd} JOGOS', '-=' * 6)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 7, '< BOA SORTE >', '-=' * 7)
