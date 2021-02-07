"""
 Módulo Collection Ordered Dict

"""
from collections import OrderedDict

# Dicionário não se preocupam com ordenação
"""dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')"""

# Ordered dict é um dicionario que se preocupa com a ordenação de inserção
"""dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')"""

# Entendendo a difereneça entre Dict e Ordered Dict

# Dict
"""dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}"""

"""print(dict1 == dict2)"""  # True -> Pois dicionarios comuns não se importam com a ordem.

# Ordered Dict
"""dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})

print(dict1 == dict2)  # False -> Pois Ordered Dict's se importam com a ordem 

"""
