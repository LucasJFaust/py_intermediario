# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         print('_____')
#         raise

# def divide(n, d):
#     if d == 0:
#         raise ZeroDivisionError ('Você está tentando dividir por zero')

#     return n / d

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError ('Você está tentando dividir por zero')
    return True

def divide(n, d):
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float.'
        )

    if not isinstance(d, (float, int)):
        raise TypeError(
            f'{d} deve ser int ou float.'
        )

    nao_aceito_zero(d)
    return n / d

print(divide(8,"0"))