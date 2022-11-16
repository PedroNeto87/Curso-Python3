'''pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 34}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
      print(k)
for k in pessoas.values():
      print(k)'''
#del pessoas['sexo'] apagar uma chave
#pessoas['nome'] = 'Leandro' modificar um elemento
'''pessoas['peso'] = 82.5 #adiciona elemento
for k, v in pessoas.items(): #substitui o enumerate
      print(f'{k} = {v}')'''
'''brasil = []
estado1 = {'uf':'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])'''
estado = {}
brasil = []
for c in range(0, 3):
      estado['uf'] = str(input('Unidade Federativa: '))
      estado['sigla'] = str(input('Sigla do estado: '))
      brasil.append(estado.copy())
for e in brasil: #laço para uma lista
      for v in e.values(): #laço para um dicionario
            print(v, end=' ')
      print()
