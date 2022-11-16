from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for c in range(1, 8):
    n = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - n
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(tmaior))
print('E também tivemos {} pessoas menores de idade'.format(tmenor))
