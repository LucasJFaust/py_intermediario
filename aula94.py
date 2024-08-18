# Generator expression
# Iterables: # Tem a responsabilidade de deter os valores de maneira sequencial
# Iterators: Tem a responsabilidade de te entregar um valor por vez, ou seja, ele precisa saber qual o próximo valor

iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__()  # tem __iter__ e __next__
iterator = iter(iterable)
print(next(iterator))