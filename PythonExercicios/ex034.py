n = float(input('Qual o salário do funcionário? R$'))
if n >= 1250:
    salario = n * 1.1
else:
    salario = n * 1.15
print('Quem ganhava R$\033[33m{:.2f}\033[m passa a ganhar R$\033[32m{:.2f}\033[m agora.'.format(n, salario))
