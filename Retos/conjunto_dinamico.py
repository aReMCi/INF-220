class Conjunto_Dinamico:

   def __init__(self, elementos = None):
      if elementos is None:
         self.elementos = []  #Inicializar una lista vacia
      else:
         self.elementos = list(elementos)  #Convertir a lista
   
   def agregar(self, elemento):
      if elemento not in self.elementos:
         self.elementos.append(elemento)  
   
   def eliminar(self, elemento):
      if elemento in self.elementos:
         self.elementos.remove(elemento)
   
   def union(self, otro_conjunto):
      nuevo_conjunto = Conjunto_Dinamico(self.elementos)
      for elemento in otro_conjunto.elementos:
         nuevo_conjunto.agregar(elemento)
      return nuevo_conjunto

   def interseccion(self, otro_conjunto):
      nuevo_conjunto = Conjunto_Dinamico()
      for elemento in self.elementos:
         if elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar(elemento)
      return nuevo_conjunto

   def pertenece(self, elemento):
      if elemento in self.elementos:
         print(f"Elemento {elemento} pertenece al conjunto.")
      else:
         print(f"Elemento {elemento} no pertenece al conjunto.")

   def diferencia(self, otro_conjunto):
      nuevo_conjunto = Conjunto_Dinamico()
      for elemento in self.elementos:
         if elemento not in otro_conjunto.elementos:
            nuevo_conjunto.agregar(elemento)
      return nuevo_conjunto
   
   def diferencia_simetrica(self, otro_conjunto):
      nuevo_conjunto = Conjunto_Dinamico()
      for elemento in self.elementos:
         if elemento not in otro_conjunto.elementos:
            nuevo_conjunto.agregar(elemento)
      for elemento in otro_conjunto.elementos:
         if elemento not in self.elementos:
            nuevo_conjunto.agregar(elemento)
      return nuevo_conjunto
   
   def ordenar(self):
      self.elementos.sort()
      print("Conjunto ordenado:", self.elementos)

   

   def __str__(self):
      return "{" + ", ".join(map(str, self.elementos)) + "}"


#Ejemplo

# Crear instancias de Conjunto_Dinamico

conjunto1 = Conjunto_Dinamico([1, 2, 3])
conjunto2 = Conjunto_Dinamico([3, 4, 5])

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

conjunto1.agregar(4)
conjunto2.eliminar(5)
conjunto2.agregar(2)
conjunto1.agregar(5)

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

conjunto2.ordenar()

conjuntou = conjunto1.union(conjunto2)
conjuntoi = conjunto1.interseccion(conjunto2)
conjuntod = conjunto1.diferencia(conjunto2)  
conjuntods = conjunto1.diferencia_simetrica(conjunto2)

print("Union:", conjuntou)
print("Interseccion:", conjuntoi)
print("Diferencia:", conjuntod)
print("Diferencia Simetrica:", conjuntods)

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
