print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print(str(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')))
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, (preco * 0.9)))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, (preco * 0.95)))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(preco / 2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, ((preco * 1.2) / parcelas)))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, (preco * 1.2)))
else:
    print('Opção Invalida!')
