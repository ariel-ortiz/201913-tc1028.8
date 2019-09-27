def potencias_de_dos(n):
    """
    >>> potencias_de_dos(5)
    (1, 2, 4, 8, 16)
    >>> potencias_de_dos(10)
    (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
    >>> potencias_de_dos(0)
    ()
    >>> potencias_de_dos(1)
    (1,)
    """
    acumulador = ()
    for i in range(n):
        acumulador += (2 ** i,)
    return acumulador