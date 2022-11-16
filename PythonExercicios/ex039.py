from datetime import date
atual = date.today().year
print(str(input('''Informe seu sexo:
[ 1 ] MASCULINO
[ 2 ] FEMININO''')))
opcao = int(input('Sua opção: '))
if opcao == 2:
    print('Você não está obrigada a se alistar.')
if opcao == 1:
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu no ano de {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = saldo + atual
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Opção inválida!')
