"""
Dicionarios

Em outras liguangens os dicionarios python são conhecidos como "mapas".
Dicionarios são coleções do tio  Chave/Valor.

Dicionarios são representados por chaves "{}"

"""

print(type({}))

# Forma comum de criação de dicionário
"""paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}"""

# print(paises)

# Forma incomum de criação de dicionário
"""paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)"""

# Acessando elementos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 1 - Acessando os elementos pela chave (incomum)
print(paises['br'])
print(paises['py'])

# Forma 2 - Acessando via get (comum)
print(paises.get('br'))
print(paises.get('ru'))

