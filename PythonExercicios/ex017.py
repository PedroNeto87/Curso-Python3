from math import hypot
co = float(input('Informe o cumprimento do cateto oposto: '))
ca = float(input('Informe o cumprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))
