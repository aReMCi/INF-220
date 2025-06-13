#Lista dinamica simple dinamica (Nodo)
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#Lista dinamica simple dinamica (Lista)

class ListaDinamica:
    def __init__(self):
        self.primero = None

    def append(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.primero:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def _buscar(self, dato):
        actual = self.primero
        while actual:
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None
    
    def mostrar(self):
        actual = self.primero
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


    def eliminar(self, dato):
        actual = self.primero
        if actual and actual.dato == dato: 
            self.primero = actual.siguiente
            actual = None
            return

    previo = None
    while actual and actual.dato != dato
        previo = actual
        actual = actual.siguiente

    if actual is None:
        return
    
    previo.siguiente = actual.siguiente
    actual = None


#Ejemplo de uso
if __name__ == "__main__":
    lista = ListaDinamica()
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.mostrar()  # Salida: 1 -> 2 -> 3 -> None

    lista.eliminar(2)
    lista.mostrar()  # Salida: 1 -> 3 -> None

    lista.eliminar(1)
    lista.mostrar()  # Salida: 3 -> None

    lista.eliminar(3)
    lista.mostrar()  # Salida: None