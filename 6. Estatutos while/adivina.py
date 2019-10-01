# Juego: Adivina un número del 1 al 100.

from random import randrange

aleatorio = randrange(1, 101)
print('Estoy pensando en un número del 1 al 100.')
print('Trata de adivinarlo en la menor cantidad de intentos.')
intentos = 0
opcion = 0
while opcion != aleatorio:
    intentos += 1
    opcion = int(input('Indica tu opción: '))
    if opcion < aleatorio:
        print('Intenta con un número más grande.')
    elif opcion > aleatorio:
        print('Intenta con un número más chico.')
    else:
        print('¡Le atinaste! \N{Smiling face with open mouth}')
        print('# de intentos:', intentos)
print('Fin de juego')
