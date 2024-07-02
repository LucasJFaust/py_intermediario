"""
List compreehension em Python

List compreehensio é uma forma rápida para criar listas a partir de iteráveis
"""

# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# Como fazer as 4 linhas de código acima usando list compreehensio:
lista = [
    numero * 2
    for numero in range(10)]
print(lista)