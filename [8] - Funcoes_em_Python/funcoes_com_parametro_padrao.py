"""
  Funções onde a passagem de parâmetros é opicional

# Evitar variaveis GLOBAIS
"""

"""# Exemplo de função com parâmetro padrão


# Funçaõ comum
def soma(num1, num2):
    return num1 + num2


# Parametro padrão - Informado como parametro uma função Soma, caso informe Subtração o retorno será diferente
def mat(num1, num2, fun=soma):
    return fun(num1, num2)


# Função comum
def subtracao(num1, num2):
    return num1 - num2


print(mat(1, 2))
print(mat(1, 2, subtracao))"""


# Podemos criar funções dentro de funções 'Funções Locais'
"""

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

# print(dentro()) # NameErros pois essa função está em escopo local dentro da função 'fora()'

"""