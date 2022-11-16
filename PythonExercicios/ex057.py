'''r = str(input('Informe seu sexo:[M/F] ')).strip().upper()[0]
while r not in 'MF':
    r = str(input('Dados invalidos. Por favor, informe seu sexo:[M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(r))'''

sexo = str(input('Informe seu sexo:[M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo:[M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
