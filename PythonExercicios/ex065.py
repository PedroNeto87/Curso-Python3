opcao = 'S'
cont = soma = media = maior = menor = 0
while opcao == 'S':
    n = int(input('Digite um valor: '))
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('Você digitou {} numeros e a media foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
