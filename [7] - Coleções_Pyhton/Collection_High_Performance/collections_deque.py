"""
  Modulo Collections -> Deque

  Deque -> É uma lista de alta performance

"""
from collections import deque

deq = deque('Andrews')
print(deq)

# Adicionando elementos no Deque
deq.append('y')  # Append adiciona no final
print(deq)

deq.appendleft('k')  # Append left adiciona no inicio da lista
print(deq)

# Remover elementos
print(deq.pop())  # Remove o ultimo elemento da lista e retorna o elemento removido
print(deq)

print(deq.popleft())  # Remove o primeiro elemento da lista e retorna o elemento removido
print(deq)
