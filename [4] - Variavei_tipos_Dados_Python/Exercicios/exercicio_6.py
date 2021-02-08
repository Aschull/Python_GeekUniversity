"""
  Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
  Fórmula: F = C * (9.0/5.0) + 32.0, sendo F a temperatuao em Fahrenheit e C a temperatura em Celsius.
"""
c = float(input())

f = c * (9.0/5.0) + 32.0

print(f'{c}° graus Celsius = {f}° Fahrenheit')
