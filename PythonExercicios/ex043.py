peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura? (M) '))
imc = peso / altura ** 2
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc <= 25:
    print('PARABÉNS, você está na faixa  de PESO IDEAL')
elif imc <= 30:
    print('Você está em SOBREPESO')
elif imc <= 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBSIDADE MÓRBIDA, CUIDADO!')
