"""

 Estruturas lógicas
 AND, OR, NOT, IS

 Lógica AND -> E
 Logica OR -> OU
 Lógica NOT -> NEGACÃO
 Lógica IS -> COMPARAÇÃO

"""

ativo = True
logado = False

print(f'Ativo: {ativo}')
print(f'Logado: {logado}\n')

# if ativo:
#    print("Usuário ativo no sistema")

# if ativo and logado:
#     print("Bem vindo usuário(a)")
# else:
#     print("Cheque seu e-mail")

# if ativo or logado:
#     print("Bem vindo usuário(a)")
# else:
#     print("Cheque seu e-mail")

# if not ativo:
#     print("Cheque seu e-mail")
# else:
#     print("Bem vindo usuário(a)")

if ativo is False:
    print("Cheque seu e-mail")
else:
    print("Bem vindo usuário(a)")
