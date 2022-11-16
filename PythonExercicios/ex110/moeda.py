def aumentar(preco=0, taxa=0, formato=False):
    resp = preco + (preco * taxa/100)
    return resp if formato is False else moeda(resp)


def diminuir(preco=0, taxa=0, formato=False):
    resp = preco - (preco * taxa/100)
    return resp if formato is False else moeda(resp)


def dobro(preco=0, formato=False):
    resp = preco * 2
    return resp if not formato else moeda(resp)


def metade(preco=0, formato=False):
    resp = preco / 2
    return resp if not formato else moeda(resp)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxa1=10, taxa2=10):
    print('-' * 30)
    print('RESUMO DE VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preco, taxa1, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preco, taxa2, True)}')
    print('-' * 30)
