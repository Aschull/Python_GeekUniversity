"""
  Modulo Collection -> Named Tuple

  #Tupla
  tupla = (1, 2, 3)
  print(tupla[1])

  Name Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e também paraêmtros
"""
from collections import namedtuple
# Pode-se criar um tipo de dado únicod essa forma, como uma classe/objeto
# Precisamos definir o nome e parâmetros

# Forma 1 - Declarando Named Tuple
# 'cachorro' -> Nome da tupla
# 'idade raca nome' ->  são 3 parâmetros dessa tupla
cachorro1 = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declarando Named Tuple
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declarando tupla
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro1(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Forma 1 - Acessando os dados
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2 - Acessando os dados
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))  # Retorna o Indice
print(ray.count('Chow-Chow'))  # Retorna a quantidade de 'Chow-Chow'
