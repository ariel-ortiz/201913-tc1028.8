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


def tripifica(tup):
    """
    Devuelve una tupla donde el primer elemento de tup aparece una vez, el
    segundo elemento aparece dos veces, y el tercer elemento aparece tres
    veces.

    >>> tripifica((1, 2, 3))
    (1, 2, 2, 3, 3, 3)
    >>> tripifica(('a', 'b', 'c', 'd', 'e'))
    ('a', 'b', 'b', 'c', 'c', 'c')
    >>> tripifica(((1, 2), (3, 4), (5, 6), (7, 8)))
    ((1, 2), (3, 4), (3, 4), (5, 6), (5, 6), (5, 6))
    >>> isinstance(tripifica((1, 2, 3)), tuple)
    True
    """
    primero = tup[0:1]
    segundo = tup[1:2] * 2
    tercero = tup[2:3] * 3
    return primero + segundo + tercero


def primera_palabra(frase):
    """
    Devuelve la primera palabra que se encuentra
    en frase.

    >>> primera_palabra('uno dos tres')
    'uno'
    >>> primera_palabra('a b c d')
    'a'
    >>> primera_palabra('1234 5678')
    '1234'
    """
    indice_espacio = frase.find(' ')
    palabra = frase[0:indice_espacio]
    return palabra


if __name__ == '__main__':
    import doctest
    doctest.testmod()
