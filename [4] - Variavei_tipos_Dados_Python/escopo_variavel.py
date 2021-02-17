"""
 Escopo variaveis

 Variavel global
 Variavel local

 Caso crie uma variavel global e dentro de um escopo fechado eu queira usar a variavel global eu posso usar a palavra
   reservada 'Global'

# Nesse caso eu criei a variavel resultado em escopo global e dentro da função 'incrementa()' eu estou informando
  que qro utilizar a variavel global ao invés de utilizar em escopo local.


 resultado = 0

 def incrementa():
     global resultado
     resultado = resultado +1

     return resultado
"""