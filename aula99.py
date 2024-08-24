# # import aula98_m

# # print(aula98_m.variavel)

# from sys import path
# import aula99_package.modulo
# from aula99_package.modulo import soma_do_modulo
# from aula99_package import modulo

# print(__name__)
# # print(*path, sep='\n')  # com o * estamos desempacotando a lista e com o \n garatimos que cada item esteja em uma linha
# print(soma_do_modulo(1,2))
# print(aula99_package.modulo.soma_do_modulo(2,3))
# print(modulo.soma_do_modulo(3,4))

# from aula99_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# print(soma_do_modulo(3, 3))
# fala_oi()

# Os packs podem ser inicialisados com um arquivo chamado __init__.py
# import aula99_package
from aula99_package import soma_do_modulo, fala_oi
# print(aula99_package.dobra(2))
print(soma_do_modulo(2, 3))
fala_oi()