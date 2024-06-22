# Exercicios com funções

"""
Crie uma função que pultiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.
"""

def multi_args(*args):
    total = 1  # Neste caso colocamos o total = a 1 e não zero, pq com o 0 teriamos um erro onde qualquer número multiplicado por 0 é igual a 0.
    for numero in args:
        total *= numero
    return total

multiplicacao = multi_args(10,2,3,4,5)
print(multiplicacao)
"""
Crie uma função que fale se um número é par ou ímpar.
Retorne se o número é par ou ímpar
"""

def par_impar(numero):
    multiplo_de_2 = numero % 2 == 0
    if multiplo_de_2:
        return f'O número {numero} é par.'
    return f'O número {numero} é impar.'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))