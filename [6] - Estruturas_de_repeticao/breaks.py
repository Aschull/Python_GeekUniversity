"""
Breaks é utilizado para forçar sair de um looping
For ou While
"""

# Exemplo
for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print("Saí do loop !")

# Exemplo 2
while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        break
