"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe escopo global e local.
-> Escopo Global: é o escopo onde todo o código é alcançavel.
-> Escopo Local: é o escopo onde penas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos do escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.
"""

# Todo código que está dentro da fução, permanesse isolado do resto do código
# É possível definir a variável em um escopo externo a função
x = 1

def escopo():
    # global x  # o uso do global é considerado uma má prática.
    x= 10  # Como estamos protegidos pelo escopo da função, não temos acesso ao x = 1

    def outra_funcao():
        # global x
        x = 11
        y = 2  # Essa variável está protegida pela segunda função. Portanto, a primeira não tem acesso.
        print(x, y)
    outra_funcao()
    # print(x)

print(x)
escopo()
print(x)