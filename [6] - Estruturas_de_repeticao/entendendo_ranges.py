"""
# Exemplo 1
range(valor_de_parada) -- por padrão o incremente é '1' e o inicio é '0'
for num in range(11):
    print(num)

# Exemplo 2
range(valor_de_inicio, valor_de_parada)

for num in range(1, 11):
    print(num)

# Exemplo 3
range(valor_de_inicio, valor_de_parada, passo) -- nesse caso o incremento será '2'
for num in range(1, 10, 2):
    print(num)

# Exemplo 4
range(valor_de_inicio, valor_de_parada, passa) -- O inverso do exemplo 3, faz uma contagem regressiva
for num in range(10, 0, -1):
    print(num)

# Criar lista com range

lista = list(range(10))
resultado -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
