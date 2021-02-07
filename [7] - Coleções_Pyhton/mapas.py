"""
  Mapas - Conhecidos em python por dicionários e são representados por chaves '{}'

"""

# Iterar Dicionarios/Mapas
"""receita = {'jan': 100, 'fev': 200, 'mar': 300}

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')"""

# Acessar chaves

"""receita = {'jan': 100, 'fev': 200, 'mar': 300}"""
"""print(receita.keys())"""

# Modo pythonico de interar
"""for chave in receita.keys():
    print(receita[chave])"""

# Acessar valores
"""receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita.values())"""

# Modo pythonico de acessar valores
"""for chave in receita.values():
    print(chave)"""

# Desempacotamento de dicionarios
"""receita = {'jan': 100, 'fev': 200, 'mar': 300}

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')"""


# Soma, valor máximo, valor mínimo e tamanho
# Os valores devem ser inteiros ou reais

receita = {'jan': 100, 'fev': 200, 'mar': 300}

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
