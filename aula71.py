"""
args -> Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembrete de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

# def soma(*args):  # Os args são tudo que passarmos para função de maneira não nomeada
#     # args = list(args)
#     print(args, type(args))

def soma(*args):
    total = 0  # O nome dessa técnica é acumulador.
    for numero in args:
        print('Total', total, numero)
        total = total + numero  # Isso é a mesma coisa que total += numero
        print('Total', total)

soma(1, 2, 3, 4, 5, 6)