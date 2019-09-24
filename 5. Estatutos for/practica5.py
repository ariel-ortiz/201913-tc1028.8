# Autor:
#          Ariel Ortiz Ramírez
#
# Funciones con estatutos for.
#
# 24 de septiembre, 2019.


def piramide(n):
    """
    Devuelve la suma de los cuadrados de 1 a n.

    >>> piramide(1)
    1
    >>> piramide(2)
    5
    >>> piramide(3)
    14
    >>> piramide(10)
    385
    >>> piramide(100)
    338350
    """
    suma = 0  # Acumulador
    for i in range(1, n + 1):
        suma += i ** 2
    return suma


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
