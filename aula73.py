"""
Higher Order Functios

Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'Bom dia', 'Lucas'))

# print(saudacao('Bom dia'))  # Aqui estamos atribuindo o texto para dentro da função que vai para o parâmetro msg