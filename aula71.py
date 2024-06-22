"""
args -> Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembrete de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

# def soma(*args):  # Os args são tudo que passarmos para função de maneira não nomeada os argumentos
#     # args = list(args)
#     print(args, type(args))

def soma(*args):  # O *args empocata o que eu enviar para a função dentro de uma tupla,  sendo uma tupla onde a gente pode passar argumentos não nomeados
    total = 0  # O nome dessa técnica é acumulador.
    for numero in args:
        total = total + numero  # Isso é a mesma coisa que total += numero
    return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6)

# Existe uma função no python chamada sum que já facilita o processo anterior

outra_soma = soma(1,2,3,4,5,6,7,78,10)
print(outra_soma)
print(sum((1,2,3,4,5,6,7,78,10)))