# Mapeamento de dados em list comprehension

# Módulo para deixar o print mais organizado
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome:': 'p1', 'preco': 20, },
    {'nome:': 'p2', 'preco': 10, },
    {'nome:': 'p3', 'preco': 30, }
]

# Exemplo alterar preços dos valores e salvar em uma outra lista:
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     for produto in produtos
# ]

# Imagina que eu quero aumentar o preço do produto, somente se ele estiver acima de 20 reais
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

# Exemplo de um filtro no list compreehension
# Eu quero incluir um número se ele for menor do que 5
# lista = [n for n in range(10) if n < 5]

# OBS: O que vem a esquerda dor for é mapeamento e a direita é filtro
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

p(novos_produtos)