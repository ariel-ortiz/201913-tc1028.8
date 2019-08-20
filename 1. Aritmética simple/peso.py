# Autor:
#          Ariel Ortiz Ramírez
#
# Calcula el peso de un objeto a partir
# de su masa.
#
# 20 de agosto, 2019.

masa = float(input('Masa del objeto en kilogramos: '))
GRAVEDAD = 9.8
peso = masa * GRAVEDAD
print('El peso de un objeto de', masa, 'kg es:', peso, 'Newtons')
