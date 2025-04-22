class monomio:
    def __init__(self, coeficiente, variable, exponente):
        self.coeficiente = coeficiente
        self.variable = variable
        self.exponente = exponente


class polinomio:
    def __init__(self, dimension, polinomio=None):
        if polinomio is not None:
            self.polinomio = polinomio
            self.dimension = len(polinomio)
        else:
            self.polinomio = []
            self.dimension = dimension

    def set_termino(self, nuevo_monomio):
        self.polinomio.append(nuevo_monomio)
        self.dimension += 1

    def get_termino(self, pos):
        if pos < 0 or pos >= len(self.polinomio):
            raise IndexError("Posición fuera de rango")
        return self.polinomio[pos]

    def get_dimension(self):
        return self.dimension

    def __str__(self):
        resultado = ""
        for i in range(len(self.polinomio)):
            if self.polinomio[i] is not None:
                resultado += f"{self.polinomio[i].coeficiente}{self.polinomio[i].variable}^{self.polinomio[i].exponente} + "
        return resultado[:-3]


# Ejemplo
monomio1 = monomio(2, "x", 2)
monomio2 = monomio(3, "x", 2)

polinomio1 = polinomio(10)
polinomio1.set_termino(monomio1)
polinomio1.set_termino(monomio2)
print(polinomio1)
print(polinomio1.get_dimension())
