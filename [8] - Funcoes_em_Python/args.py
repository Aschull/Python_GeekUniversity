"""
  Entendendo *args

  O parametro *args informados em uma função coloca os valores extras
  em uma tupla (valores se tornam imutáveis)

"""

# Exemplo comum


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


# print(soma_todos_numeros(2, 3, 4))


"""def soma_todos_numeros2(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total"""

# Refatorando pois args tratam de tuplas


# def soma_todos_numeros2(*args):
#     """
#     Recebe uma cadeia de números, soma todos os elementos em tuplas e retorna a soma
#     :param args: números
#     :return: soma dos elementos da tupla
#     """
#     return sum(args)

"""print(soma_todos_numeros2())
print(soma_todos_numeros2(1))
print(soma_todos_numeros2(1, 2))
print(soma_todos_numeros2(1, 2, 3))
print(soma_todos_numeros2(1, 2, 3, 4))
print(soma_todos_numeros2(1, 2, 3, 4, 5))"""


# Outro exemplo de utilização de *args
# Sabendo que *args é uma tupla, podemos utilizar todas as funções
#   e métodos de trabalho utilizado em tuplas

"""def verifica_info(*args):
    if 'Andrews' in args and 'Fernandes' in args:
        return 'Bem vindo Andrews'
    return 'Não sei quem é vc!'


print(verifica_info())
print(verifica_info(1, True, 'verdade', 'Andrews'))
print(verifica_info('Fernandes', 3.145, 'Andrews'))"""

# Desempacotador com *args
# *args só trabalha com tuplas e n com listas
# Ao utilizar o '*' antes da variável, o Python desempacota a lista e atribu valor por valor em uma tupla
#  podendo assim efetuar as operações.

numeros = [1, 2, 3, 4, 5, 6, 7]


def soma_todos_num(*args):
    return sum(args)


print(soma_todos_num(*numeros))





