"""
Estruturas de repetição

"FOR"

Exemplos de iteraveis
  String
    nome = "Andrews Schulla Fernandes"
  Lista
    lista = [1, 2, 3, 4, 5]
  Range
    numeros = range[1, 10]
"""

nome = 'Andrews Schulla Fernandes'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)  # Temo que transormar em lista


"""print('Exemplo 1 - Iterando sobre uma String')
for letra in nome:
    print(letra)
print('\n')"""


"""print('# Exemplo 2 - Iterando sobre uma lista')
for num in lista:
    print(num)
print('\n')"""


"""print('# Exemplo 3 - Iterando sobre um range')
for num in range(1, 10):
    print(num)
print('\n')"""

"""print('# Exemplo 4 - Iterando com enumerate')
nome = 'Andrews Schulla Fernandes'
for i, n in enumerate(nome):
    print(nome[i])

nome = 'Andrews Schulla Fernandes'
for _, n in enumerate(nome):
    print(n)

nome = 'Andrews Schulla Fernandes'
for n in enumerate(nome):
    print(n)"""

"""qtd = int(input('Quantas vezes o loop deve rodar? '))

for n in range(1, qtd+1):
    print(f'Imprimendo {n}')"""

"""qtd = int(input('Quantas vezes o loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}--{qtd} valor: '))
    soma = soma + num
print(f'A soma é: {soma}')"""

# Imprimir emojis

# Unicode original - U+1F60D
# Unicode modificado - U0001F60D

for num in range(1, 11):
    print('\U0001F60D' * num)