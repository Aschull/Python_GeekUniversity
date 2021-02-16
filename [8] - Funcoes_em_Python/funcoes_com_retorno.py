"""
  Funções com retorno
"""
from random import random

num = [1, 2, 3]

x = num.pop()


# print(num)
# print(x)

def quadrado_de_7():
    return 7 ** 2


x = quadrado_de_7()


# print(x)

# Número pseudo randomico(pois pode retornar números repetidos)
def cara_coroa():
    # Função random() gera números pseudo-randomicos entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


# print(cara_coroa())

# Função Ímpar/Par
def impar_par():
    numero = 6
    if numero % 2 != 0:
        return 'Ímpar'
    return 'Par'


print(impar_par())
