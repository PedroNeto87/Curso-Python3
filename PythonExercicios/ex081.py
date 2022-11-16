lista = []
element = 0

#while True:
    #lista.append(int(input('Digite um valor: ')))
    #resp = str(input('Quer continuar?[S/N] '))
    #if resp == 'Nn':
        #break
#print(f'Você digitou {len(lista)} elementos)'
#lista.sort(reverse=True)
#print(f'Os valores em ordem decrescente {lista}')
#if 5 in lista:
    #print('O valor 5 faz parte da lista!')
#else:
    #print('O valor 5 não faz parte da lista.')

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
        element += 1
    else:
        print('Valor duplicado! Não vou adicionar.')
    cont = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Você digitou {element} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')
