# =========================================================
# A. Ortiz, 2019-08-16
#
# Primer programa en Python. Ejemplo de gráficas de 
# tortuga.
# =========================================================

from turtle import forward, right, left, done, pensize, pencolor

# Dibujar un cuadrado rojo de líneas gordas.
pencolor('red')
pensize(10)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

# Dibuja un triángulo azul de líneas medianas.
pencolor('blue')
pensize(5)
right(120)
forward(100)
right(120)
forward(100)

done()
