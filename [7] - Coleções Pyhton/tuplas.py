"""
Tuplas são muito parecidas com listas

Existem duas diferenças básicas entre tuplas e listas

1 - As tuplas são representadas por parênteses '()'
2 - As tuplas são imutáveis, isso é: Ao criar uma tupla ela não muda, toda operação com tuplas
      irão gerar uma nova tupla.
"""

# Warning: As tuplas são representadas por '()', mas perceba:
# Cria tupla
"""tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))"""

# Cria tupla, msm sem o parênteses
"""tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))"""

# Warning: Tuplas com 1 elemento
"""tupla3 = (4)
print(tupla3)"""
# tupla3 n é uma tupla, o python enxerga isso como um 'int'
"""print(type(tupla3))"""

# tupla4 é uma tupla de um elemento apenas.
"""tupla4 = (4,)
print(tupla4)
print(type(tupla4))"""

"""tupla5 = 5,
print(tupla5)
print(type(tupla5))"""
# Conclusão: Tuplas são representadas por parênteses '()' mas são definidas pela vígurla ','.

# Gerar tupla dinâmicamente com range(inicio,fim,passo)
"""tupla = tuple(range(11))
print(tupla)
print(type(tupla))"""

# Desempacotamento de tupla
"""tupla = 'Andrews', 'Schulla', 'Fernandes'

nome, sobrenome, ultimo_nome = tupla
print(nome)
print(sobrenome)
print(ultimo_nome)"""

# Métodos para adição e remoção de elementos em tuplas não existem pois as tuplas são imutáveis

# Pode-se realizar: *Soma, verificar Valor Máximo, Valor Mínimo e Tamanho desde que para as operações
#                     de Soma, Valor Máximo e Valor Mínimo sejam para uma tupla de valores inteiros ou reais

"""tupla1 = (1, 2, 3, 4, 5, 6)
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))"""

# Concatenação de tuplas
# Tuplas são imutáveis mas podemos alterar os seus valores.
"""tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = (tupla1 + tupla2)
print(tupla1)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)
print(tupla3)

print(3 in tupla1)
"""

# Iteração em tuplas
"""tupla1 = (1, 2, 3)

for num in tupla1:
    print(num)

for indice, valor in enumerate(tupla1):
    print(indice, valor)"""



