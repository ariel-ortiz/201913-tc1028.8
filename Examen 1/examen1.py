# Solución al primer examen.


def temperatura(fahrenheit):
    """
    Devuelve una tupla con la conversión
    de fahrenheit a celsius y kelvin.

    >>> temperatura(212)
    (100.0, 373.15)
    >>> temperatura(77)
    (25.0, 298.15)
    >>> temperatura(32)
    (0.0, 273.15)
    >>> isinstance(temperatura(32), tuple)
    True
    """
    celsius = 5 / 9 * (fahrenheit - 32)
    kelvin = celsius + 273.15
    return (celsius, kelvin)


def reemplaza_vocales_por_a(frase):
    """
    Convierte frase a minúsculas y reemplaza
    toda las vocales por la letra "a".

    >>> reemplaza_vocales_por_a('Una MOSCA parada en la pared.')
    'ana masca parada an la parad.'
    >>> reemplaza_vocales_por_a('hasta mañana, jaja!')
    'hasta mañana, jaja!'
    >>> reemplaza_vocales_por_a('aeiou')
    'aaaaa'
    >>> isinstance(reemplaza_vocales_por_a('aeiou'), str)
    True
    """
    minusculas = frase.lower()
    reemplaza_e = minusculas.replace('e', 'a')
    reemplaza_i = reemplaza_e.replace('i', 'a')
    reemplaza_o = reemplaza_i.replace('o', 'a')
    reemplaza_u = reemplaza_o.replace('u', 'a')
    return reemplaza_u


if __name__ == '__main__':
    import doctest
    doctest.testmod()
