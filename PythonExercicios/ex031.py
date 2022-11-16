n = float(input('Qual é a distância da sua viagem em KM? '))
print('Você está prestes a começar sua viagem de {:.1f}KM.'.format(n))
if n < 200:
    preço = n * 0.5
else:
    preço = n * 0.45
print('E o preço da sua passagem será de \033[4mR${:.2f}'.format(preço))
