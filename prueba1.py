class Numero:
    def __init__(self, numero):
        self.numero = numero

    def FijarValor(self, Valor):
        self.numero = Valor

    def ObtenerValor(self):
        return self.numero
    
    def CantidadNumeros(self):
        return len(str(self.numero))
    
    def VerifPar(self):
        return self.numero % 2 == 0

    def UltimoDigito(self):
        return self.numero % 10
    
    def add_digit(self, digit):
        self.numero = self.numero * 10 + digit
        return self.numero
    
    def delete_last_digit(self):
        self.numero = self.numero // 10
        return self.numero

    def __str__(self):
        return str(self.numero)
            

# Crear una instancia de la clase Numero
mi_numero = Numero(0)

# Pedir al usuario que ingrese un valor
print("Ingrese un valor para el numero: ")
Valor = int(input())

# Fijar el valor del numero
mi_numero.FijarValor(Valor)

# Mostrar el valor del numero
print("El valor del numero es: ", mi_numero)

# Mostrar la cantidad de digitos del numero
print("La cantidad de digitos del numero es: ", mi_numero.CantidadNumeros())

# Verificar si el numero es par o impar
if mi_numero.VerifPar():
    print("El numero es par")
else:
    print("El numero es impar")

# Mostrar el valor del ultimo digito del número
print("El ultimo digito es: ", mi_numero.UltimoDigito())

# Pedir al usuario que ingrese un digito
print("Ingrese un digito para agregar al numero: ")
digito = int(input())
print("El digito fue ingresado exitosamente")

# Agregar el digito al numero y mostrar el nuevo valor
nuevo_valor = mi_numero.add_digit(digito)
mi_numero.FijarValor(nuevo_valor)
print("El nuevo valor del numero es: ", mi_numero)

# Eliminar el último dígito del número y mostrar el nuevo valor
nuevo_valor = mi_numero.delete_last_digit()
mi_numero.FijarValor(nuevo_valor)  
print("El nuevo valor del numero es: ", mi_numero)
