nome = str(input('Qual seu nome? '))
if nome == 'Pedro':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'Paulo' or nome == 'João':
    print('Seu nome é bem normal no Brasil.')
elif nome in 'Creuza':
    print('Que nome feio!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
