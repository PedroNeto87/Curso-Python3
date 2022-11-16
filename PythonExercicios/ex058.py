from random import randint
computador = randint(0, 10)
'''from time import sleep
computador = randint(0, 10)
tentativa = 0
print('\033[33m-=-\033[m'*20)
print('\033[1;34mVou pensar em um numero de 0 a 10. Tente advinhar...\033[m')
print('\033[33m-=-'*20)
jogador = int(input('\033[1;37mEm que numero pensei?\033[m '))
print('\033[35mPROCESSANDO...\033[m')
sleep(0.5)
while jogador != computador:
    jogador = int(input('Você errou, tente novamente! Em que numero pensei? '))
    tentativa += 1
print('\033[32mPARABÉNS! Você conseguiu me vencer! Você usou {} tentativas!\033[m'.format(tentativa + 1))'''
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. PARABÉNS'.format(palpite))
input('Precione "ENTER" para sair!')
