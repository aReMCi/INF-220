class monomio:
    def __init__(self, coeficiente, variable, exponente):
        self.coeficiente = coeficiente
        self.variable = variable
        self.exponente = exponente

class polinomio:
    def __init__(self, dimension =10, monomios = None):
        if not isinstance(monomios, list):
            raise TypeError("Los monomios deben ser una lista")
        if dimension < 10:
            raise ValueError("El polinomio no puede tener menos de 10 monomios")
        self.dimension = dimension
        self.monomios = monomios[:dimension]

    def Agregar_termino(self, nuevo_monomio):
        if self.dimension == len(self.monomios):
            raise ValueError("El polinomio ha alcanzado su dimension maxima")
        if not isinstance(nuevo_monomio, monomio):
            raise TypeError("El monomio debe ser de tipo monomio")
        
        self.monomios.append(nuevo_monomio)

    def Get_termino(self,pos):
        pos = pos-1
        if pos < 0 or pos >= len(self.monomios):
            raise IndexError("Posición fuera de rango")
        return self.monomios[pos]    
    
    def __str__(self):
        return " + ".join([f"{monomio.coeficiente}{monomio.variable}^{monomio.exponente}" for monomio in self.monomios])

#Ejemplo
monomio1 = monomio(2, "x", 2)
monomio2 = monomio(3, "x", 2)

polinomio1 = polinomio(10, [])
polinomio1.Agregar_termino(monomio1)
polinomio1.Agregar_termino(monomio2)

term = polinomio1.Get_termino(2)
print(f"El primer monomio es: {term.coeficiente}{term.variable}^{term.exponente}")

