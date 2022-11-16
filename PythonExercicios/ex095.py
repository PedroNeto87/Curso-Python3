time = []
dados = {}
gol = []
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    n = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gol.clear()
    for c in range(0, n):
        gol.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dados['gols'] = gol[:]
    dados['total'] = sum(gol)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 22)
print('Cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 45)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 45)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 - Parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}!')
    else:
        print(f'  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 45)
print('<<< VOLTE SEMPRE >>>')
