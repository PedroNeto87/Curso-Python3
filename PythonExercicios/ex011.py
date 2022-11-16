n1 = float(input('Qual a altura da parede? '))
n2 = float(input('Qual a largura da parede? '))
p = n1 * n2
print('Area total da parede: {} M²'.format(p))
tinta = p / 2
print('Sabemos que são gastos 1 litro de tinta para cada 2M², então serão necessários {} LTs de tinta para pintar '
      'toda a parede.'.format(tinta))
