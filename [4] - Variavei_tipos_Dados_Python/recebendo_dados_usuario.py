"""
Recebendo dados do usuário

"""
# print("Qual o seu nome ?")
# nome = input()

nome = input("Qual o seu nome ?")

# print("Qual sua idade ?")
# idade = input()

idade = int(input("Qual a sua idade ?"))

# Forma antiga de print versão 2.xxxx
# print("O(a) %s, tem %s anos" % (nome, age))

# Print moderno versão 3.xxxx
# print("O {0}, tem {1} anos".format(nome, age))

# Forma atual de print a partir da versão 3.7.xxx
print(f'O {nome}, tem {idade} anos')

# Utilizando cast int na saída dos dados
# print(f'{nome} nasceu no ano de {2021 - int(idade)}')

# Utilizando cast int na declaração da variável
print(f'{nome} nasceu no ano de {2021 - idade}')
