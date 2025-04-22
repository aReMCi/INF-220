import pickle
import os
import shutil


class conjunto_persistente:
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(filename):
            with open(filename, "r") as file:
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

    def Copia_de_seguridad(self):
        respaldo = self.filename + ".bak"
        shutil.copy(self.filename, respaldo)
        print(f"Copia de seguridad creada: {respaldo}")

    def limpiar(self, bandera):
        if bandera == 1:
            self.Copia_de_seguridad()
            self.elementos.clear()
            self.guardar()
            # Archivo limpiado dejando un archivo de respaldo
        elif bandera == 2:
            self.elementos.clear()
            self.guardar()
            # Archivo limpiado sin respaldo

    def contiene(self, elemento):
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
        nuevo_conjunto.elementos = self.elementos.symmetric_difference(
            otro_conjunto.elementos
        )
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    def guardar(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.elementos, file)

    def mostrar(self):
        print("Conjunto:", self.elementos)


# Ejemplo

# Crear instancia de conjunto_persistente
conjunto1 = conjunto_persistente("conjunto1.dat")
conjunto1.agregar(2)
conjunto1.agregar(3)
conjunto1.agregar(4)
conjunto1.mostrar()

conjunto2 = conjunto_persistente("conjunto2.dat")
conjunto2.agregar(3)
conjunto2.agregar(4)
conjunto2.agregar(5)
conjunto2.mostrar()

conjunto1.union(conjunto2).mostrar()
