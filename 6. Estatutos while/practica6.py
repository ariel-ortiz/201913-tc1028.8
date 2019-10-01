# Práctica #6: Estatutos de repetición for y while.


def duplica(frase):
    """Devuelve una nueva cadena en la que cada
    carácter de frase está duplicada.

    >>> duplica('Hola')
    'HHoollaa'
    >>> duplica('')
    ''
    >>> duplica('¡Me gusta programar!')
    '¡¡MMee  gguussttaa  pprrooggrraammaarr!!'
    >>> duplica('ESTO SE ACABÓ')
    'EESSTTOO  SSEE  AACCAABBÓÓ'
    >>> isinstance(duplica('Hola'), str)
    True
    """
    resultado = ''
    for caracter in frase:
        resultado += (caracter + caracter)
    return resultado


def periodos(inicial, objetivo, interes):
    """Devuelve el número de periodos de inversión
    necesarios para que el saldo inicial crezca a un
    monto que sea igual o superior al saldo objetivo
    dada la tasa de interes.

    >>> periodos(200, 250, 0.05)
    5
    >>> periodos(15000, 14000, 0.07)
    0
    >>> periodos(15000, 15000, 0.07)
    0
    >>> periodos(15000, 30000, 0.05)
    15
    >>> periodos(15000, 30000, 0.07)
    11
    >>> periodos(15000, 30000, 1.00)
    1
    >>> isinstance(periodos(200, 250, 0.05), int)
    True
    """
    num_periodos = 0
    saldo = inicial
    while saldo < objetivo:
        num_periodos += 1
        saldo += (saldo * interes)
    return num_periodos


def complemento_inverso_adn(hebra):
    """Devuelve una cadena de caracteres con el
    complemento inverso de hebra, todo en mayúsculas.

    >>> complemento_inverso_adn('GATTACA')
    'TGTAATC'
    >>> complemento_inverso_adn('tctgttgagt')
    'ACTCAACAGA'
    >>> complemento_inverso_adn('TtCcTtaGGtcTCCAgccGc')
    'GCGGCTGGAGACCTAAGGAA'
    >>> complemento_inverso_adn('')
    ''
    >>> isinstance(complemento_inverso_adn('GATTACA'), str)
    True
    """
    acumulador = ''
    for caracter in hebra.upper():
        if caracter == 'A':
            acumulador += 'T'
        elif caracter == 'T':
            acumulador += 'A'
        elif caracter == 'C':
            acumulador += 'G'
        elif caracter == 'G':
            acumulador += 'C'
    inverso = acumulador[::-1]
    return inverso


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
