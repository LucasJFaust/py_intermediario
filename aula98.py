# Modularização

# Entendendo os seus próprios módulos Python
# O primeiro módulo executado se chama __main__
# Podemos importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

# try:
#     import sys
#     sys.path.append('/home')
# except ModuleNotFoundError:
#     ...

# print(*sys.path, sep='\n')

import aula97_m
from aula97_m import variavel_modulo, soma

print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula97_m.soma(2, 4))


