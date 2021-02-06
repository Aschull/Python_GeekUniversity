"""
Dicionarios

Em outras liguangens os dicionarios python são conhecidos como "mapas".
Dicionarios são coleções do tio  Chave/Valor.

Dicionarios são representados por chaves "{}"

"""

# Forma comum de criação de dicionário
"""paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}"""

# print(paises)

# Forma incomum de criação de dicionário
"""paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)"""

# Acessando elementos
"""paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
"""
# Forma 1 - Acessando os elementos pela chave (incomum)
"""print(paises['br'])
print(paises['py'])"""

# Forma 2 - Acessando via get (comum - recomendado)
"""print(paises.get('br'))
print(paises.get('ru'))"""

"""paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
"""
"""russia = paises.get('ru', 'Não encontrado')  # Caso n encontre 'ru', exibe o valor 'Não encontrado'
pais = paises.get('br')"""

"""print(f'Encontrei o país: {russia}')
print(f'Encontrei o país: {pais}')"""


# Quando utilizado 'get', se o elemento informado não existe no dicionario
#   o get ira retornar a pesquisa como None, None no python é sempre considerar como false.
# Exemplo:
"""if None:
    print('TRUE - None')
else:
    print('FALSO')"""

# Verificando se a chave se encontra no dicionario
"""paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print('br' in paises)
print('ru' in paises)
# Ele busca pela chave e não pelo valor portanto 'Estados Unidos' é False
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
"""

# Podemos utilizar qualquer tipo de dados como chaves de dicionario
# Utilizando tupla como chave. (reomendado pois tuplas são imutáveis
"""localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7794, 122.4194): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))"""

# Adicionar elementos em dicionários
"""receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))"""

# Forma 1 (comum)
"""receita['abr'] = 350
print(receita)"""

# Forma 2 (incomum)
"""novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)"""


# Atualizando dados em um dicionário

# Forma 1
"""receita['mai'] = 550
print(receita)"""

# Forma 2
"""receita.update({'mai': 770})
print(receita)"""

# A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# Em dicionários, NÃO podem ter chaves repetidas.

# Remover dados de um dicionário

"""receita = {'jan': 100, 'fev': 120, 'mar': 300}"""

# Forma 1 (pop()) - (comum)
"""retorno = receita.pop('mar') # Deve-se passar a chave
print(receita)
print(retorno)"""
# Ao remover um objeto, o valor do objeto é retornado tbm.

# Forma 2 - Não retorna valor do objeto
"""del receita['fev']
print(receita)"""

# Aplicabilidade de dicionários

# Carrinho de compras Carrinho com Lista - (possível mas n muito comum pois necessitaria saber os indices de cada
# produto e suas informações)

"""carrinho = []

produto1 = ['Ps4', 1, 1600.00]
produto2 = ['God of War', 1, 79.90]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)"""

# Carrinho com Tupla (possível mas n muito comum pois necessitaria saber os indices de cada produto e suas informações)
"""produto1 = ('Ps4', 1, 1600.00)
produto2 = ('God of War', 1, 79.90)

carrinho = (produto1, produto2)

print(carrinho)"""

# Carrinho com Dicionário (Para esse caso, DIcionário é o recomendado)
"""carrinho = []

produto1 = {'nome': 'Ps4', 'quantidade': 1, 'preco': 1600.00}
produto2 = {'nome': 'God Of War', 'quantidade': 1, 'preco': 79.90}

# carrinho = (produto1, produto2)
carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)"""

# Metodos para Dicionário

"""d = dict(a=1, b=2, c=3)
print(d)"""

# Limpar dicionario
"""d.clear()"""

# Copiando dicionario para outro
# Forma 1
"""novo['d'] = 4
novo = d.copy() # Deep Copy
print(novo)"""

# Forma 2 - Shallow Copy

"""novo = d
novo['d'] = 4

print(d)
print(novo)"""

# Forma não usual de criação de dicionários
"""outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))"""

# Nome, pontos, email, profile são chaves, desconhecido é o valor de todas essas chaves
"""usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))"""

# Metodo fromkeys() recebe 2 parâmetros, um iterável e um valor
# Ele va gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

# Nesse caso, a chave 'Teste' por ser uma string, é um iterável, sendo assim,
#   cada letra de 'teste' ser´uma chave com o valor 'valor'.
# O resultado de chaves será "tes" pq dicionários não pode ter chaves duplicadas
"""veja = {}.fromkeys('teste', 'valor')
print(veja)"""

# Utilizando range
"""veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)"""






