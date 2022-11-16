n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media <= 4.9:
    print('Aluno REPROVADO')
elif 5 <= media < 7:
    print('Aluno em RECUPERAÇÃO')
elif media >= 7:
    print('Aluno APROVADO')
