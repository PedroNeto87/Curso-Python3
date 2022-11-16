n = soma = tentativas = 0
n = int(input('Digite um numero - [999 para parar]: '))
while n != 999:
    tentativas += 1
    soma += n
    n = int(input('Digite um numero - [999 para parar]: '))
print('Fim do programa, você digitou {} numeros e a soma entre eles foi {}!'.format(tentativas, soma))
