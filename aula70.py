"""
Retorno de valores das funções (return)
"""
def soma(x, y):
    if x > 10:
        return 10, 20
    return x + y  # O return é diferente do print. O print só exibe algo na tela. O return deixa disponível valores para manipulação, deixando a expressão criada, disponível.

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))