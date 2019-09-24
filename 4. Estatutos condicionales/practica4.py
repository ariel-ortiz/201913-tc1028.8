# Autor:
#          Ariel Ortiz Ramírez
#
# Funciones con estatutos condicionales.
#
# 13 de septiembre, 2019.

from math import sqrt, isclose


def signo(n):
    """
    Determina el signo de n.

    Devuelve -1 si n es negativo, 1 si n es positivo
    mayor que cero, o 0 si n es igual a cero.

    >>> signo(-5)
    -1
    >>> signo(10)
    1
    >>> signo(0)
    0
    >>> isinstance(signo(0), int)
    True
    """
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


def sort3(a, b, c):
    """
    Devuelve una tupla con los valores de a, b y c en orden ascendente.

    >>> sort3(-34, 16, 25)
    (-34, 16, 25)
    >>> sort3(-34, 25, 16)
    (-34, 16, 25)
    >>> sort3(16, -34, 25)
    (-34, 16, 25)
    >>> sort3(16, 25, -34)
    (-34, 16, 25)
    >>> sort3(25, -34, 16)
    (-34, 16, 25)
    >>> sort3(25, 16, -34)
    (-34, 16, 25)
    >>> sort3(25, 25, 25)
    (25, 25, 25)
    >>> sort3(-25, 25, 25)
    (-25, 25, 25)
    >>> sort3(25, -25, 25)
    (-25, 25, 25)
    >>> sort3(25, 25, -25)
    (-25, 25, 25)
    >>> isinstance(sort3(-25, 25, 25), tuple)
    True
    """

    if a <= b <= c:
        return (a, b, c)
    elif a <= c <= b:
        return (a, c, b)
    elif b <= a <= c:
        return (b, a, c)
    elif b <= c <= a:
        return (b, c, a)
    elif c <= a <= b:
        return (c, a, b)
    else:
        return (c, b, a)


def tipo_de_triangulo(p1, p2, p3):
    """
    Determina el tipo de un triángulo con los puntos p1, p2, p3.

    >>> tipo_de_triangulo((1, 2), (2, 3), (4, 2))
    'escaleno'
    >>> tipo_de_triangulo((1, 1), (2, 3), (3, 1))
    'isósceles'
    >>> tipo_de_triangulo((1, 3), (1, 5), (1 + 3 ** 0.5, 4))
    'equilátero'
    >>> tipo_de_triangulo((5, 5), (3, 5), (3, 1))
    'rectángulo'
    >>> isinstance(tipo_de_triangulo((5, 5), (3, 5), (3, 1)), str)
    True
    """
    (x1, y1) = p1
    (x2, y2) = p2
    (x3, y3) = p3

    a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    (a, b, c) = sort3(a, b, c)

    if isclose(a ** 2 + b ** 2, c ** 2):
        return 'rectángulo'
    elif isclose(a, b) and isclose(b, c):
        return 'equilátero'
    elif isclose(a, b) or isclose(b, c) or isclose(a, c):
        return 'isósceles'
    else:
        return 'escaleno'


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
