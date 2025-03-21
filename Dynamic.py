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
deposito(100)
retiro(50)
deposito(200)

ver_historial()
print(f"El balance de la cuenta es: {balance()}")