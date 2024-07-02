# Outra funcionalidade da list compreehension é a possíbilidade de fazermos um for dentro do outro utilizando o lado direito

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))  # Não é possível dentro de uma lista colocar 2 dados sem especificar o tipo desses dados, por isso determinamos x, y

# Fazendo com o list compreehension
# lista = [
#     (x, y)
#     x for x in range(3) 
#     for y in range(3)
# ]
# print(lista)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)