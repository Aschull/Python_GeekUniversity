"""
 Módulo Collections -> Default Dict

 dicionario = {'curso': 'programação em python: Essencial'}
 print(dicionario)
 print(dicionario['curso])
 print(dicionario['outro']) # Gera keyError

 Ao usar o Default Dict, nós informamos um valor default, podendo utilizar lambda.
 Este valor será utilizado quando não houver um valor definido.
 Caso tente acessar um valor inexistente, o default dict irá criar a chave e atribuirá o valor default


 Lambdas -> São funções sem nome, que podem ou não receber parâmetros de entrada
              e retornar valores.
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro'])
print(dicionario)




