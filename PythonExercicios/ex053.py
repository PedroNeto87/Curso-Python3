frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
# inverso = junto[::-1] *Maçete de fatiamento, também funciona!
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALINDROMO!')
else:
    print('NÃO temos um PALINDROMO!')
