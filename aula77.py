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

pessoa = {
    'nome': 'Lucas José',
    'sobrenome': 'Faust Machado',
    # 'idade': 900,
}

print(len(pessoa))
print(pessoa.keys())
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))
pessoa.setdefault('idade', 20)
print(pessoa['idade'])

for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)