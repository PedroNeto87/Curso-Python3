import math
n = float(input('Informe o ângulo que você deseja: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tang = math.tan(math.radians(n))
print('O ângulo {} tem o Seno de {:.2f}'.format(n, sen))
print('O ângulo {} tem o Cosseno de {:.2f}'.format(n, cos))
print('O ângulo {} tem a Tangente de {:.2f}'.format(n, tang))
