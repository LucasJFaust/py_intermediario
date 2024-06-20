"""
Introdução a funções (def) em Python

Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar valores específicos.
Por padrão, funções Python retornam None (nada).
"""
# A função pode receber parâmetros dentro dos (). Esses parâmetros podem receber valores em algum momento,
# quando o parâmetro recebe o valor ele passa a ser referido como argumento. Argumento é o valor passado para o parâmetro no momento da execução da função.


# def Print(a, b, c):
#     print('Várias')

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome= 'Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Lucas José')
saudacao('Pedro')
saudacao('Rafael')
saudacao()