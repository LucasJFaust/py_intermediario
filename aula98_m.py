print(123)

import aula98_m

variavel = 'Lucas'

# Módulos no python são singleton, ou seja únicos. O python guarda um módulo importado na memória e disponibiliza ele novamente para ser mais eficiente.
# for i in range(10):
#     print(i)
#     import aula98_m

# print('Fim')

# Para recarregar um módulo precisamos usar o importlib
import importlib

for i in range(10):
    print(i)
    importlib.reload(aula98_m)

print('Fim')