dados = {}
gol = []
total = 0
dados['nome'] = str(input('Nome do jogador: '))
n = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, n):
    gol.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total += 1
dados['gols'] = gol[:]
dados['total'] = sum(gol)
print('-=-' * 16)
print(dados)
print('-=-' * 16)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 16)
print(f'O jogador {dados["nome"]} jogou {n} partidas.')
for i, v in enumerate(gol):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
