"""
String python

. EM python um dado é considerado uma string sempre q estiver entre:
. Aspas simlpes
. Aspas duplas
. Aspas simples triplas
. Aspas duplas triplas

"""
# Quebra de linha

nome = "Angelina \nJolie"
print(nome)

nome = """Angelina 
Jolie"""
print(nome)


nome = "Angelina Jolie"
print(nome)

# Comece do primeiro elemeto ':', vá até o ultimo elemento ':' e inverta eles '-1'
print(nome[::-1])

# Replace de letras
print(nome.replace("n", "o"))

# Verificar o tipo da variavel
print(type(nome))
