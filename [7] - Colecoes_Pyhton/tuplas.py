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

# Concatenando elementos dentro de uma tupla
"""tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))"""

# Transforma String em Tupla
"""escola = tuple('Geek University')
print(escola)
print(escola.count('e'))"""

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre q não precisarmos modificar os dados contidos em uma coleção

# Exemplos:
# Meses do ano
"""meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
print(meses)"""

# O acesso a elemetos de uma tupla também é semelahnte a de uma lista
"""print(meses[5])"""

# Interar com while
"""i = 0
while i < len(meses):
    print(meses[i])
    i += 1"""

# Verificar em qual indice um elemento se encontra na tupla
"""print(meses.index('Junho', 3))"""

# Caso o elemento não exista na tupla ir gerar um ERRO

# Slicing
"""meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
# tupla[inicio:fim:passo]
print(meses[5:9:1])"""

"""# Pq utilizar tuplas ??
# - Tuplas possuem maior performance em comparação a listas
# - Tuplas deixam seu código mais seguro por conta da imutabilidade.
"""

"""# Copiando uma tupla para outra
# Em tuplas não existem Shallow copy
tupla = (1, 2, 3)
print(tupla)
nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(tupla)"""
