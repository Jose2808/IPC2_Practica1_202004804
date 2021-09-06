from Nodo import Nodo

class Cola:
    def __init__ (self):
        self.inicio = None

    def agregarOrden(self, ingrediente):
        nueva_orden = Nodo(ingrediente)
        if self.inicio is None:
            self.inicio = nueva_orden
        else:
            puntero = self.inicio 
            while puntero.siguiente is not None:
                puntero = puntero.siguiente
            puntero.siguiente = nueva_orden

    def desplegarOrdenes(self):
        if self.inicio is not None:
            puntero = self.inicio
            while puntero is not None:
                print(puntero.ingrediente)
                puntero = puntero.siguiente
        else:
            print("Cola vacía - No hay ordenes en curso para mostrar\n")

    def entregarOrden(self):
        if self.inicio is not None:
            aux = self.inicio
            self.inicio = self.inicio.siguiente
            print("Entregando orden de pizza de:" + aux.ingrediente)
        else:
            print("Cola vacía - Totalidad de órdenes entregadas\n")