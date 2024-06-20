"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} z={z}', '|', 'x + y = ', x + y + z)

# Argumento posicional
soma(1, 2, 3)

# Argumentos nomeados
soma(y=2, z=3, x=1)