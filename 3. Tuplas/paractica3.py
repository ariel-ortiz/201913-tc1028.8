# Autor:
#          Ariel Ortiz Ramírez
#
# Funciones que manipulan tuplas.
#
# 6 de septiembre, 2019.


def incrementa(n):
    """
    Devuelve una tupla conformada por cuatro números: n seguido de n
    más uno, seguido de n más dos, seguido de n más tres.

    >>> incrementa(1)
    (1, 2, 3, 4)
    >>> incrementa(100)
    (100, 101, 102, 103)
    >>> incrementa(8.2)
    (8.2, 9.2, 10.2, 11.2)
    >>> incrementa(-5)
    (-5, -4, -3, -2)
    >>> isinstance(incrementa(5), tuple)
    True
    """
    n_mas_1 = n + 1
    n_mas_2 = n + 2
    n_mas_3 = n + 3
    return (n, n_mas_1, n_mas_2, n_mas_3)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
