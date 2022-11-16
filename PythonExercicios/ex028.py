from random import randint
from time import sleep
Computador = randint(0, 5) #faz o computador "pensar"
print('\033[33m-=-\033[m' * 20),
print('\033[1;34mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
jogador=int(input('\033[1;37mEm que número pensei?\033[m ')) #jogador tenta adivinhar
print('\033[35mPROCESSANDO...\033[m')
sleep(2)
if jogador == Computador:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!\033[m'.format(Computador, jogador))
