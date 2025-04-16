''''
Clase polinonmio de tipo ADT Estatico
Creamos primero la clase monomio y luego la clase polinomio
'''

class monomio:
    def __init__(self,coeficiente,variable,exponente):
        self.coeficiente = coeficiente
        self.variable = variable
        self.exponente = exponente
        self.siguiente = None

class polinomio:
    def __init__(self,monomio,dimension):
        if not isinstance(monomio, list):
            raise TypeError("Los monomios deben ser una lista")
        if dimension < 10:
            raise ValueError("El polinomio no puede tener menos de 10 monomios")
        self.dimension = dimension
        self.cabeza = None
        self.dim_actual = 0

    def Agregar_termino(self, nuevo_monomio):
        if self.dim_actual == self.dimension:
            raise ValueError("El polinomio ha alcanzado su dimension maxima")
        if not isinstance(nuevo_monomio, monomio):
            raise TypeError("El monomio debe ser de tipo monomio")
        
        #Si la lista esta vacia, el nuevo monomio se convierte en la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_monomio
        else:   
            #Recorremos la lista hasta encontrar el ultimo monomio
            #y lo enlazamos con el nuevo monomio
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_monomio
        self.dim_actual += 1

    def Mostrar(self):
        if self.cabeza is None:
            print("El polinomio esta vacio")
            return
        actual = self.cabeza
        while actual is not None:
            print(f"{actual.coeficiente}{actual.variable}^{actual.exponente}", end=" ")
            actual = actual.siguiente
        print()
    

#Ejemplo

monomio1 = monomio(2,"x",2)
monomio2 = monomio(3,"x",2)

polinomio1 = polinomio([],10)
polinomio1.Agregar_termino(monomio1)
polinomio1.Agregar_termino(monomio2)
polinomio1.Mostrar()

        

    


    