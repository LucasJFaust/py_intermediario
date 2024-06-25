"""
Métodos úteis dos dicionários em python
-> len - quantas chaves
-> keys - iterável com as chaves
-> values - iterável com os valores
-> items - iterável com chaves e valores
-> setdefault - adicioa valor se a chave não existe
-> copy - retorna uma cópia rasa (shallow copy)
-> get - obtém uma chave
-> pop - apaga um item com chave específica (del)
-> popitem - apaga o último item adicionado
-> update - atualiza um dicionário com outro
"""

p1 = {
    'nome': 'Lucas José',
    'sobrenome': 'Faust Machado',
    # 'idade': 900,
}

# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': '30',
# })

# p1.update(nome='novo valor', idade=30)

tupla = ('nome', 'novo valor'), ('idade', 30)
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(tupla)