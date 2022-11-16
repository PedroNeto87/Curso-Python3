n1 = float(input('Informe a KM percorrida? '))
n2 = int(input('Informe a quantidade de dias: '))
s = (n1 * 0.15) + (n2 * 60)
print('O valor total a pagar pelo uso do veículo é de: R${:.2f}'.format(s))
