import random

class NodoArbol:
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            aux = self.raiz
            ant = None
            while aux is not None:
                ant = aux
                if dato <= aux.info:
                    aux = aux.izq
                else:
                    aux = aux.der

            if dato <= ant.info:
                ant.izq = NodoArbol(dato)
            else:
                ant.der = NodoArbol(dato)

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.info, end=' ')
            self.preorden(nodo.izq)
            self.preorden(nodo.der)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izq)
            print(nodo.info, end=' ')
            self.inorden(nodo.der)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.info, end=' ')

    def buscar(self, nodo, buscado):
        if nodo is None:
            return None
        if nodo.info == buscado:
            return nodo
        if buscado < nodo.info:
            return self.buscar(nodo.izq, buscado)
        return self.buscar(nodo.der, buscado)

    def eliminar(self, dato):
        pass  # Implementación de la función eliminar

    def altura(self, nodo):
        if nodo is None:
            return -1
        else:
            return 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

    def ocurrencias(self, nodo, elemento):
        if nodo is None:
            return 0
        count = 0
        if nodo.info == elemento:
            count = 1
        return count + self.ocurrencias(nodo.izq, elemento) + self.ocurrencias(nodo.der, elemento)

    def contar_pares_impares(self, nodo):
        if nodo is None:
            return (0, 0)
        pares_izq, impares_izq = self.contar_pares_impares(nodo.izq)
        pares_der, impares_der = self.contar_pares_impares(nodo.der)
        if nodo.info % 2 == 0:
            return (1 + pares_izq + pares_der, impares_izq + impares_der)
        else:
            return (pares_izq + pares_der, 1 + impares_izq + impares_der)

def main():
    arbol = Arbol()
    for _ in range(1000):
        arbol.insertar(random.randint(1, 10000))

    print("Barrido preorden:")
    arbol.preorden(arbol.raiz)
    print("\n\nBarrido inorden:")
    arbol.inorden(arbol.raiz)
    print("\n\nBarrido postorden:")
    arbol.postorden(arbol.raiz)
    print()

    buscado = 500
    resultado = arbol.buscar(arbol)
