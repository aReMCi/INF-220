class monomio:
    def __init__(self, coeficiente, variable, exponente):
        self.coeficiente = coeficiente
        self.variable = variable
        self.exponente = exponente

class polinomio:
    def __init__(self, dimension =10, polinomio = None):
        if not isinstance(polinomio, list):
            raise TypeError("El polinomio debe ser una lista")
        if dimension > 10:
            raise ValueError("El polinomio no puede tener más de 10 términos")
        self.dimension = dimension
        self.polinomio = polinomio[:dimension]
    
    def set_termino(self, pos, nuevo_monomio):
        pos= pos-1
        if not isinstance(nuevo_monomio, monomio):
            raise TypeError("El monomio debe ser de tipo monomio")
        if pos <= self.dimension:
            self.polinomio[pos] = nuevo_monomio
        else:   
            raise IndexError("Posición fuera de rango")

    def Get_termino(self,pos):
        if pos < 0 or pos >= len(self.polinomio):
            raise IndexError("Posición fuera de rango")
        return self.polinomio[pos]    

    def __str__ (self):
        resultado = ""
        for i in range(len(self.polinomio)):
            if self.polinomio[i] is not None:
                resultado += f"{self.polinomio[i].coeficiente}{self.polinomio[i].variable}^{self.polinomio[i].exponente} + "
        return resultado[:-3] #Elimina el último " + "

#Ejemplo
monomio1 = monomio(2, "x", 2)
monomio2 = monomio(3, "x", 2)
monomio3 = monomio(4, "x", 1)

polinomio1 = polinomio(10, [])
polinomio1.set_termino(1, monomio1)
polinomio1.set_termino(2, monomio2)
print(polinomio1)
term = polinomio1.Get_termino(1)
print(f"EL termino {term.coeficiente}{term.variable}^{term.exponente}")