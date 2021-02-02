# Errado... "vírgula" gera tupla, para float é usado "ponto"
valor = 1, 44
print(valor)
print(type(valor))

# Certo no ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Para criar variaveis complexas utiliza "j"
print("Tipo complexo")
var = 5j
print(type(var))

# Tipo complexo elevado ao quadrado
var = var ** 2
print(var)

# Conversão de tipo inteiro para float

print("Conversão int to float")
var_int = 3
print(float(var_int))
