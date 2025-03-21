transacciones = []

def deposito(monto):
    transacciones.append({'type' : 'deposito', 'monto' : monto})

def retiro(monto):
    transacciones.append({'type' : 'retiro', 'monto' : monto})

def ver_historial():
    for transaccion in transacciones:
        print(f"{transaccion['type']}: {transaccion['monto']}")

def balance():
    balance = 0
    for transaccion in transacciones:
        if transaccion['type'] == 'deposito':
            balance += transaccion['monto']
        elif transaccion['type'] == 'retiro':
            balance -= transaccion['monto']
            
    return balance

#Ejemplo
print("Bienvenido al banco")
Bandera = True
while Bandera == True:
    print("¿Que desa hacer?")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Salir")
    if input() == '1':
        print("¿Cuanto desea depositar?")
        deposito(int(input()))
    elif input() == '2':
        print("¿Cuanto desea retirar?")
        retiro(int(input()))
    elif input() == '3':
        Bandera = False
    else:
        print("Opcion no valida")   

ver_historial()
print(f"El balance de la cuenta es: {balance()}")