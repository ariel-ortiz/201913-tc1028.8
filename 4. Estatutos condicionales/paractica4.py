# Autor:
#          Ariel Ortiz Ramírez
#
# Funciones con estatutos condicionales.
#
# 13 de septiembre, 2019.


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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
