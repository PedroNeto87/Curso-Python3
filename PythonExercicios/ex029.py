v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    print('\033[1;31mMULTADO!\033[m \033[31mVocê excedeu o limite de velocidade que é de 80KM/H')
    print('Você deve pagar uma multa de\033[m \033[1;41mR${:.2f}\033[m\033[31m!\033[m'.format((v - 80) * 7))
print('\033[33mBom dia, dirija com segurança!\033[m')
