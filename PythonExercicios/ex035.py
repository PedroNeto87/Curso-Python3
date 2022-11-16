print('\033[32;43m-=-\033[m' * 8)
print('\033[1;32mAnalisador de Triângulos\033[m')
print('\033[32;43m-=-\033[m' * 8)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3 +r1 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
