"""
  Funções que recebem dados de entrada
"""


"""def soma(x, y):
    return x + y


print(soma(3, 5))"""


"""def outra(num1, b, msg):
    return (num1 + b) * msg


print(outra(2, 8, 'teste'))"""

# Diferença entre parametros e argumentos
# Parâmetros - São variáveis declaradas na definição de uma função
# Argumentos - São dados passados durante a execução de uma função


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [3, 6, 5, 2, 2, 1]
print(soma_impares(lista))
