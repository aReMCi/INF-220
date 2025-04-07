'''
Representación de una ADT Estatica de un objeto automovil
La clase Automovil tiene los siguientes atributos: 
- power: si el automovil esta encendido o apagado
- estado: si el automovil esta en movimiento o parado
- velocidad: la velocidad del automovil
- marcha: la marcha en la que se encuentra el automovil
- direccion: la direccion en la que se encuentra el automovil
'''
class Automovil:
    #Constructor de la clase automovil
    def __init__(self, power="Apagado", estado="Parado", velocidad=0, marcha=None, direccion=None):
        self.power = power
        self.estado = estado
        self.velocidad = velocidad
        self.marchas = ["P", "R", "N", "D"]
        self.marcha = marcha if marcha in self.marchas else "P"
        self.direccion = direccion  

# Metodos getter y setter para automovil
    
    def get_power(self):
        return self.power
    
    def get_estado(self):
        return self.estado 
       
    def get_velocidad(self):
        return self.velocidad
    
    def get_marcha(self):
        return self.marcha
    
    def get_direccion(self):
        return self.direccion
    
    def set_power(self, power):
        self.power = power

    def set_estado(self, estado):    
        self.estado = estado

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_marcha(self, marcha):
        self.marcha = marcha

    def set_direccion(self, direccion):
        self.direccion = direccion
        
# Metodos de la clase automovil
# Encender el automovil
    def encender(self):
        if self.get_power() == "Apagado":
            self.set_power("Encendido")
            self.set_estado("Parado")
            self.set_velocidad(0)
            self.set_marcha("D")
            print("El automovil esta encendido, en marcha D")
        else:
            print("El automovil ya esta encendido")

# Apagar el automovil
    def apagar(self):
        if self.get_power() == "Encendido":
            self.set_power("Apagado")
            self.set_estado("Parado")
            self.set_velocidad(0)
            self.set_marcha("P")
            print("El automovil esta apagado y en marcha P")
        else:
            print("El automovil ya esta apagado")

# Acelerar el automovil
    def acelerar(self, velocidad, direccion):
        if (self.get_power() == "Encendido") and (self.get_marcha() == "D"):
            if self.get_estado() == "Parado":
                self.set_estado("En movimiento")
                self.set_direccion(direccion)
            self.set_velocidad(self.get_velocidad() + velocidad)
            print(f"El automovil acelera a {self.get_velocidad()} km/h en direccion {self.get_direccion()}")
        elif (self.get_power() == "Encendido") and (self.get_marcha() != "D"):
            print("El automovil no puede acelerar porque no esta en marcha D")  
        else:
            print("El automovil esta apagado")

# Frenar el automovil
    def frenar(self):
        if self.get_power() == "Encendido":
            if self.get_estado() == "En movimiento":
                self.set_velocidad(0)
                self.set_estado("Parado")
                self.marcha = "N"
                print("El automovil ha frenado, está parado y en marcha N")
            else:
                print("El automovil ya esta parado")
        else:
            print("El automovil esta apagado")