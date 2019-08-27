# Autores:
#          Ariel Ortiz Ramírez
#
# Funciones que usan operaciones con cadenas
# de carácteres.
#
# 3 de septiembre, 2019.


def primeras_tres_letras(palabra):
    """
    Devuelve una cadena con los tres primeros
    caracteres de palabra convertidos a
    mayúsculas.

    >>> primeras_tres_letras('Python')
    'PYT'
    >>> primeras_tres_letras('ingeniero')
    'ING'
    >>> primeras_tres_letras('programa es fácil')
    'PRO'
    >>> primeras_tres_letras('uno dos cinco')
    'UNO'
    >>> isinstance(primeras_tres_letras('uno dos cinco'), str)
    True
    """
    tres_letras = palabra[0:3]
    mayusculas = tres_letras.upper()
    return mayusculas


def iniciales(nombre, paterno, materno):
    """
    Devuelve una cadena con las iniciales en
    mayúsculas de una persona que tiene
    nombre, paterno y materno.

    >>> iniciales('Benito Pablo', 'Juárez', 'García')
    'BJG'
    >>> iniciales('Salma Valgarma', 'Hayek', 'Jiménez')
    'SHJ'
    >>> iniciales('Andrés Manuel', 'López', 'Obrador')
    'ALO'
    >>> iniciales('Octavio', 'Paz', 'Lozano')
    'OPL'
    >>> isinstance(iniciales('Octavio', 'Paz', 'Lozano'), str)
    True
    """
    inicial_nombre = nombre[0]
    inicial_paterno = paterno[0]
    inicial_materno = materno[0]
    junto_todo = (inicial_nombre
                  + inicial_paterno
                  + inicial_materno)
    mayusculas = junto_todo.upper()
    return mayusculas


if __name__ == '__main__':
    import doctest
    doctest.testmod()
