"""
Listas
 # Funcionam como vetores/matrizes/(arrays - em outras linguagens), com a dierença de serem DINÂMICOS e aceitarem
 QUALQUER tipo de dado.

 Em [C / Java]: Arrays possuem tamanhos e tipos fixos.

# [Python] - Dinâmico: Não possuem tamanho fixo: Ao criar a lista podemos inserir quantos elementos quisermos sem a
                         necessidade de por um limite de quantos elementos máximos a lista deve possuir.
                       Não possuem tipo fixo de dados, podendo inserir qualquer tipo de dado, int, string, boolean etc.

# Listas em python são representadas por colchetes "[]".

"""
"""type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['A', 'n', 'd', 'r', 'e', 'w', 's', ' ', 'S', 'c', 'h', 'u', 'l', 'l', 'a', ' ', 'F', 'e', 'r', 'n', 'a', 'n',
          'd', 'e', 's']
lista3 = []
lista4 = list(range(11))
lista5 = list('Andrews Schulla Fernandes')"""

# Verificando determinado valor em uma lista
"""num = 11
if num in lista4:
    print(f'Contém o número {num} na lista')
else:
    print(f'Não contém o número {num} na lista.')"""

"""letter = 'e'
if letter in lista5:
    print(f'Contém a letra {letter} na lista')
else:
    print(f'Não contém a letra {letter} na lista.')"""

# Ordenar lista (Primeiro ordenar depois imprimir se não o resultado é 'None')
"""lista1.sort()
print(lista1)

lista5.sort()
print(lista5)"""

# Contar quantidade de registros na lista
"""print(lista5.count('e'))"""

# Adicionar elementos em lista - append
"""lista1.append(33)
lista1.sort()
print(lista1)"""

# lista1.append(1, 4, 56, 72, 34, 12) # Isso gera ERRO, append só aceita 1 elemento por vez
# Mas aceita que informe um elemento do tipo lista, sendo assim podemos informar uma lista dentro de um lista
"""lista1.append([32, 22, 51, 67]) # Informa um elemento por vez ou uma lista em um indice, criando uma "Sub-Lista"
# lista1.sort() - Não ordena, gera ERRO
print(lista1)
"""
"""if [32, 22, 51, 67] in lista1:
    print('Contém')
else:
    print('Não contém')"""
# Adiciona mais de um elemento a lista sem a necessidade de informar uma nova lista como no append.
# .extend não aceita valor único, para valroes únicos utiliza-se o .append
# .extends só aceita tipos iteraveis como uma lista númerica ou uma string
"""lista1.extend([123, 44, 67])
print(lista1)"""

# Adiciona elemento na lista informando o valor e a posição da lista
# - Insert n subistitui o valor, se eu incluo um valor na posição 3, o valor inicial nessa posição será deslocado
#     para a posição 4 e assim por diante
"""lista1.insert(3, 777)
print(lista1)"""

#  Concatena listas
"""lista6 = lista1 + lista2"""

# Inverter valores de uma lista .reverse()
# Forma 1
"""lista1.reverse()"""

# Forma2
# slice em string
"""print(lista1[::-1])"""

# Copiar lista
"""lista6 = lista2.copy()"""

# Tamanho da lista
"""print(len(lista1))"""

# Remove o ultimo elemento da lista pop()
# O pop(), n só remove o ultimo elemento da lista mas ele retorna o ultimo elemento
"""lista5.pop()"""
# Remover pelo indice
"""lista5.pop(2)"""

# Remover todos os elementos da lista .clear()
"""lista5.clear()"""

# Trnasformar uma string em lista
"""curso = 'Aula de programação em pyhton, do iniciante ao avançado'
curso = curso.split()
print(curso)"""

# Convertendo lista em uma string
"""curso = ['Programação', 'essencial', 'em', 'Python']
curso = ' '.join(curso) # precisa de espaço entre as aspas simples ' ' ou clocar qualquer outro separador: $, ou - etc..
print(curso)"""

# Iterar lista
# for
"""for elemento in lista1:
    print(elemento)"""

# while
"""carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair":')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)"""

# Para acessar os elementos de uma lista preicsa ser de forma indexada:
#           0         1        2        3
"""cores = ['verde', 'amarelo', 'azul', 'branco']"""

"""print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco"""

# Fazer acesso aos elementos de forma indexada inverso

"""print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verder
# print(cores[-5])  # ERRO, não existe o indice 5."""

# Indice negativo da a entender que a lista trabalha como um circulo ou uma fila circular.


"""cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1"""

# Gerar indice para lista em um for
# Listas aceitam valores repetidos
"""
cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)"""

# ---------------Metodos n tão importantes mas úteis--------------- #
# Encontrar o indice de um elemento na lista
"""
numeros = [5, 6, 7, 5, 8, 9, 10]
# Em qual indice se encontra o valor 6 ?
print(numeros.index(6))

# Em qual indice se encontra o valor 9 ?
print(numeros.index(9))

# Em qual indice se encontra o valor 19 ? - ERRO, valor n existe na lista
print(numeros.index(19))

# Se eu quiser retornar o indice do valor 5, a função .indexa() retornará o primeiro 5 da lista
print(numeros.index(5))

# Buscar dentro de um range, informando a partir de qual indice iniciar a busca.
print(numeros.index(5, 1))  # Busca o valor 5 a partir do indice 1
# QUando n encontra gerar ERRO

# Bucar dentro de um range de valores
print(numeros.index(8, 3, 6))  # Busca o indice do valor 8 entre os indices 3 e 6
"""

# Revisão de slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# lista = [1, 2, 3, 4]

# Trabalhando com slice de lista com o parâmetro 'inicio'
# print(lista[1:])  # Iniciando no indice 1 e pegando todos os elementos restantes
# print(lista[-1:])  # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com parâmetro 'fim'
# print(lista[:3])   # Inicia em 0 e termina em 3.
# print(lista[:-1])  # Inicia em 0 e termina em 4 (fila circular).
# print(lista[1:3])  # Inicia em 1 e termina em 3.

# Trabalhado com parâmetro 'passo'
# print(lista[1::2])  # Inicia em 1, vai até o final, de 2 em 2.
# print(lista[::2])   # Inicia em 0, vai até o final, de 2 em 2.
# print(lista[1::-1])   # Inicia em 4, vai até o inicio, de 1 em 1 (inverte a lista).

# Soma*, valormáximo*, valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais

"""lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma
print(max(lista))  # valor máximo
print(min(lista))  # valor mínimo
print(len(lista))  # tamanho da lista"""

# Transformar lista em tupla
"""lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
"""
# Desempacotamento de lista
"""lista = [1, 2, 3, 4]
num1, num2, num3, num4 = lista

print(num1)
print(num2)
print(num3)
print(num4)"""

# Cópia de lista para outra (Shallow Copy $ Deep Copy)
# Deep Copy - Quando utilizado copy de uma lista para outra, cria-se uma nova lista
#               independente da primeira, todas as operações na cópia não afetam a lista origem.
"""lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)"""

# Shallow copy - Quando n utilizado a função copy(), as alterações feitas na lista 'nova'
#                  se refletiram na lista 'lista', dando a entender que não é criado uma nova lista
#                  e sim criado uma nova "View" da lista principal, toda alteração em suas 'Filhas' alterão
#                  a lista 'Pai'.
"""lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)

print(lista)
print(nova)"""

"""print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)"""
