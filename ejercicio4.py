import random

class Generador:
    def __init__(self, numeros, modo):
        self.numeros = numeros
        self.modo = modo

    def leer_numero(self, ini, fin, mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                if ini <= valor <= fin:
                    return valor
                else:
                    print(f"Error: El valor debe estar entre {ini} y {fin}.")
            except ValueError:
                print("Error: Debes ingresar un número.")

    def generar_numeros(self):
        lista_numeros = [random.uniform(0, 100) for _ in range(self.numeros)]
        lista_redondeada = []

        for numero in lista_numeros:
            if self.modo == 1:
                redondeado = int(numero) + (1 if numero % 1 > 0 else 0)
            elif self.modo == 2:
                redondeado = int(numero)
            else:
                redondeado = int(numero + 0.5)

            print(f"{numero} -> {redondeado}")
            lista_redondeada.append(redondeado)

        return lista_redondeada

def main():
    generador = Generador(
        numeros=generador.leer_numero(1, 20, "¿Cuántos números quieres generar? [1-20]: "),
        modo=generador.leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    )

    lista = generador.generar_numeros()
    print("Lista de números redondeados:", lista)

if __name__ == "__main__":
    main()
