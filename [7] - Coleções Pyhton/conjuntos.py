"""
 Conjuntos em programação faz referencia a teoria dos conjuntos na matemática.
 Em python, conjuntos são chamados de Sets.

- Sets (conjuntos) não possuem valores ordenados;
- Sets (conjuntos) não possuem valores duplicados;
- Elementos não são acessados via indice ou seja não são indexados.

 Utilizados quando não precisamos nos preocupar com a ordem dos elementos
 Ou quando não precisamos nos preocupar com Chave/Valor.

 Sets (conjuntos) são representados por chaves '{}'

 Diferença de Sets (conjuntos) e Mapas (Dicionarios) em python:
  - Dicionario tem chave/valor
  - Conjuntos tem apenas valor.

"""

# Definindo um conjuntos
# Forma 1
"""s = set({1, 2, 3, 4, 5, 6, 7, 2, 3, })
print(s)
print(type(s))"""
# Ao criar um conjuntos, caso informe dados repetidos, os dados repetidos serão ignorados e não farão parte do conjunto

# Forma 2 - Comun
"""s = {1, 2, 3, 4, 5, 6, 7, 2, 3}
print(s)
print(type(s))"""

# Converter Lista, String, Tuplas em conjunto
"""s = set('Andrews Schulla Fernandes')
print(s)"""

"""lista = [1, 2, 3, 4, 5, 6, 7, 2, 3, 4]
print(set(lista))"""

"""tupla = (1, 2, 3, 4, 5, 6, 7, 2, 3, 4)
print(set(tupla))"""

"""if 3 in lista:
    print('Tem o 3')
else:
    print('Não tem o 3')"""

# Conjuntos não se preocupam com ordenação

# Listas aceitam valores duplicados
"""lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista}')"""

# Tuplas aceitam valores duplicados
"""tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla}')"""

# Dicionarios não aceitam CHAVES duplicadas
"""dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario}')"""

# Conjuntos não aceitam VALORES duplicados
"""conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto}')"""


# Assim como toda outra coleção em Python podemos colocar tipos misturados em Sets (conjuntos)
"""s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))"""


# Iterar Set(conjunto)
"""for valor in s:
    print(valor)"""


# Usos de Sets
# Exemplo:
# Formulário de cadastro em um museu

# Retornar as cidades de cada visitiante
"""cidades = ['BH', 'SP', 'CWB', 'SP', 'CWB', 'SJP', 'ARA']
print(cidades)
print(len(cidades))"""

# Retornar a quantidade de cidades distintas
"""print(len(set(cidades)))"""
# Usa-se o SET pois ele trará a distinção pois não aceita repetição de valores.

# Adicionadno elementos em um conjunto
"""s = {1, 2, 3}
s.add(4)
s.add(4)  # Não insere, mas tbm n gera erro
print(s)"""

# Remover eleemntos de um Set
"""s = {1, 2, 3}
print(s)"""

# Forma 1
"""s.remove(3)  # Não é indice, é o valor a ser removido, Sets não são indexados ou seja n possui indices.
print(s)"""

# Forma 2
"""s.discard(2)
print(s)"""

# Forma 3
"""s.pop()
print(s)"""

# Copiando um conjunto para outro
"""s = {1, 2, 3}"""

# Forma 1 - Deep Copy
"""novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)"""

# Shallow Copy - Altera os valroes tanto do novo conjunto quanto do conjunto a ser copiado
# Forma 2 - Shallow Copy
"""novo = s
print(novo)

novo.add(4)
print(novo)
print(s)"""

# Remover todos os itens de um conjunto
"""s = {1, 2, 3}
s.clear()
print(s)"""

# Métodos matemáticos de conjuntos
# Alguns alunos que estudam Python, também estudam Java.
"""estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}"""

# Gerar conjunto com nomes de estudantes únicos (UNION)
# Forma 1 - Union (Recomendado)
"""unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)"""

# Forma 2 - Caractere pipe '|'
"""unicos2 = estudantes_python | estudantes_java
print(unicos2)"""

# Gerar um conjunto de estudandos que estão em ambos os cursos (INTERSECTION)
# Forma 1 - Intersection
"""ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)"""

# Forma 2 - Caractere E comercial '&'
"""ambos2 = estudantes_python & estudantes_java
print(ambos2)"""

# Gerar um conjunto de estudantes que não se encontram no outro curso (DIFFERENCE)
# Forma 1 - Difference
"""so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)"""

# Soma, Maior Valor, Menor Valor, Tamanho
"""s = {1, 2, 3, 4, 5}"""
# Soma
"""print(sum(s))"""
# Maior Valor
"""print(max(s))"""
# Menor Valor
"""print(min(s))"""
# Tamanho
"""print(len(s))"""
