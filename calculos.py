# calculos.py

from operaciones import Operaciones

operaciones = Operaciones()

a, b, c, d = (10, 5, 0, "Hola")

print("{} + {} = {}".format(a, b, operaciones.suma(a, b)))
print("{} - {} = {}".format(b, d, operaciones.resta(b, d)))
print("{} * {} = {}".format(b, b, operaciones.producto(b, b)))
print("{} / {} = {}".format(a, c, operaciones.division(a, c)))
