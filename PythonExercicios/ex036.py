casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento: '))
prestação = casa / (financiamento * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, financiamento, prestação))
if prestação <= (salario * 0.3):
    print('Emprestimo pode ser \033[1;32mCONCEDIDO!\033[m')
else:
    print('Emprestimo \033[1;31mNEGADO!\033[m')
