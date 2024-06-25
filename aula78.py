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
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# d2 = d1

# d2 = d1.copy()  # O uso do copy cria um novo dict no d2. Contudo isso é uma cópia rasa. Ou seja, tudo que for imutável ele vai copiar.
# Se tiver uma lista ele não vai copiar pois os valores são mutáveis. Acaba que ambos dicionários apontam para o mesmo local da memória.

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 9999
print(d1)
print(d2)