lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# tuplas são imutáveis ex: lanche [1] = Refrigerante
#Obs: Posso ter dados diferentes dentra das tuplas ex: pessoa = ('Gustavo', 39, 'M', 99.88)
#del(lanche) = apaga da memoria...
#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b
#print(c)
#print(c.index(8)) = mostra a posição no '8'.
#print(c.count(5)) = conta quantos numeros '5' tem na tupla.
#print(sorted(lanche)) Imprime organizado por ordem alfabetica!

#Se não precisar de posição é mais simples:
#for comida in lanche:
#    print(f'Eu vou comer {comida}')

#Seprecisar de posição tem duas formas:
#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Eu comi pra caramba!')
