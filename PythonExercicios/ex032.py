from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1m{}\033[m é \033[1;32mBISSEXTO\033[m'.format(ano))
else:
    print('O ano \033[1m{}\033[m \033[1;31mNÃO É BISSEXTO'.format(ano))
