import pickle
import os

class conjunto_persistente:
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.elementos = pickle.load(file)
        else:
            self.elementos = set()

    def agregar(self, elemento):
        self.elementos.add(elemento)
        self.guardar()
    
    def eliminar(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
            self.guardar()
    
    def contiene (self, elemento):
        return elemento in self.elementos
    
    def union(self, otro_conjunto):
        nuevo_conjunto = conjunto_persistente(self.filename)
        nuevo_conjunto.elementos = self.elementos.union(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    def interseccion(self, otro_conjunto):
        nuevo_conjunto = conjunto_persistente(self.filename)
        nuevo_conjunto.elementos = self.elementos.intersection(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    def diferencia(self, otro_conjunto):
        nuevo_conjunto = conjunto_persistente(self.filename)
        nuevo_conjunto.elementos = self.elementos.difference(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    def diferencia_simetrica(self, otro_conjunto):
        nuevo_conjunto = conjunto_persistente(self.filename)
        nuevo_conjunto.elementos = self.elementos.symmetric_difference(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    def guardar(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.elementos, file)

    def mostrar(self):
        print("Conjunto:", self.elementos)


#Ejemplo

conjunto1 = conjunto_persistente("conjunto1.dat")
conjunto1.agregar(2)
conjunto1.agregar(3)
conjunto1.agregar(4)
conjunto1.mostrar() 
