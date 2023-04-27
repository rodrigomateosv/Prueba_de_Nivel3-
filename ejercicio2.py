class Heap(object):
    """Crea un montículo"""

    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio

    def agregar(self, dato):
        self.vector[self.tamanio] = dato
        self.flotar(self.tamanio)
        self.tamanio += 1

    def quitar(self):
        self.intercambio(0, self.tamanio-1)
        dato = self.vector[self.tamanio-1]
        self.tamanio -= 1
        self.hundir(0)
        return dato

    def heap_vacio(self):
        return self.tamanio == 0

    def flotar(self, indice):
        while(indice > 0 and self.vector[indice][0] > self.vector[(indice - 1) // 2][0]):
            padre = (indice - 1) // 2
            self.intercambio(indice, padre)
            indice = padre

    def hundir(self, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while(control and hijo_izq < self.tamanio):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < self.tamanio):
                if self.vector[hijo_der][0] > self.vector[hijo_izq][0]:
                    aux = hijo_der
            if (self.vector[indice][0] < self.vector[aux][0]):
                self.intercambio(indice, aux)
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False

    def arribo(self, dato, prioridad):
        self.agregar([prioridad, dato])

    def atencion(self):
        return self.quitar()[1]

    def intercambio(self, indice1, indice2):
        self.vector[indice1], self.vector[indice2] = self.vector[indice2], self.vector[indice1]

class nodoPila(object):
    """Clase nodo pila"""

    info, sig = None, None

class Pila(object):
    """Clase Pila"""

    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato):
        """Apila el dato sobre la cima de la pila"""
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima
        self.cima = nodo
        self.tamanio += 1

    def desapilar(self):
        """Desapila el elemento en la cima de la pila y lo devuelve"""
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1
        return x

    def pila_vacia(self):
        """Devuelve true si la pila esta vacia"""
        return self.cima is None

# A continuación se encuentra el código principal que utiliza las clases Pedido, Heap y Pila:

if __name__ == "__main__":
    main()
