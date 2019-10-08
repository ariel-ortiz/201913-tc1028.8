# ----------------------------------------------------------
#
# Escribe aquí tu matrícula y nombre.
#
# ----------------------------------------------------------

def paridad(bits):
    """Devuelve bits concatenado con su correspondiente bit de paridad.

    >>> paridad('1000110')
    '10001101'
    >>> paridad('1011001')
    '10110010'
    >>> paridad('0000000')
    '00000000'
    >>> paridad('1111111')
    '11111111'
    >>> paridad('0010000')
    '00100001'
    >>> paridad('1101111')
    '11011110'
    >>> isinstance(paridad('1101111'), str)
    True
    """
    # Escribe a continuación tu solución:
    pass


def babilonico(n):
    """Calcula la raíz cuadrada de n usando el algoritmo babilónico.

    >>> babilonico(2)
    1.414213562373095
    >>> babilonico(4)
    2.0
    >>> babilonico(5)
    2.23606797749979
    >>> babilonico(256)
    16.0
    >>> isinstance(babilonico(1), float)
    True
    """
    # Escribe a continuación tu solución:
    pass


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
