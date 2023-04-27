# operaciones.py

class Operaciones:
    def suma(self, a, b):
        try:
            return a + b
        except TypeError:
            print("Error: Tipo de dato no válido.")
            return None

    def resta(self, a, b):
        try:
            return a - b
        except TypeError:
            print("Error: Tipo de dato no válido.")
            return None

    def producto(self, a, b):
        try:
            return a * b
        except TypeError:
            print("Error: Tipo de dato no válido.")
            return None

    def division(self, a, b):
        try:
            return a / b
        except TypeError:
            print("Error: Tipo de dato no válido.")
            return None
        except ZeroDivisionError:
            print("Error: No es posible dividir entre cero.")
            return None
