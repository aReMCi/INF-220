class Conjunto_Estatico:
    def __init__(self,elementos, dimension = 10):
        if not isinstance(elementos, list):
            raise TypeError("Los elementos deben ser una lista")
        if len(elementos) > dimension:
            raise ValueError(f"El conjunto no puede tener más de {dimension} elementos")
        self.elementos = elementos[:dimension]
        self.dimension = dimension

    def union(self, otro_conjunto):
        elementos_unidos = list(set(self.elementos) | set(otro_conjunto.elementos))
        return Conjunto_Estatico(elementos_unidos)
    
    def interseccion(self, otro_conjunto):
        elementos_intersec = list(set(self.elementos) & set(otro_conjunto.elementos))
        return Conjunto_Estatico(elementos_intersec)

    def diferencia(self, otro_conjunto):
        elementos_diff = list(set(self.elementos) - set(otro_conjunto.elementos))
        return Conjunto_Estatico(elementos_diff)

    def diferencia_simetrica(self, otro_conjunto):
        elementos_diff_sim = list(set(self.elementos) ^ set(otro_conjunto.elementos))
        return Conjunto_Estatico(elementos_diff_sim)

    def pertenece(self, elemento):
        if elemento in self.elementos:
            print(f"Elemento {elemento} pertenece al conjunto.")
        else:
            print(f"Elemento {elemento} no pertenece al conjunto.")

    def es_subconjunto(self, otro_conjunto):
        return set(self.elementos).issubset(set(otro_conjunto.elementos))
    
    def contiene(self,elemento):
        return elemento in self.elementos

    def modificar_elemento(self, pos, nuevo_elemento):
        if pos < 0 or pos >= len(self.elementos):
            raise IndexError("Posición fuera de rango")
        self.elementos[pos-1] = nuevo_elemento
        self.ordenar()

    def ordenar(self):
        self.elementos.sort()
        print("Conjunto ordenado:", self.elementos)
    
    def __str__(self):
        return str(self.elementos)

#Ejemplo
conjunto1 = Conjunto_Estatico([1, 2, 3])
conjunto2 = Conjunto_Estatico([3, 4, 5])

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

conjuntou = conjunto1.union(conjunto2)
conjuntoi = conjunto1.interseccion(conjunto2)
conjuntod = conjunto1.diferencia(conjunto2)
conjuntods = conjunto1.diferencia_simetrica(conjunto2)

print("Unión:", conjuntou)
print("Intersección:", conjuntoi)   
print("Diferencia:", conjuntod) 
print("Diferencia Simétrica:", conjuntods)

conjunto1.modificar_elemento(2,4)
print("Conjunto 1", conjunto1)
print("Conjunto 2", conjunto2)
