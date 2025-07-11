
# 🔍 ¿Qué encapsula este código?
# __saldo es una variable privada, usada internamente para proteger el estado de la cuenta.
# Los métodos depositar y retirar controlan el acceso al saldo y validan las operaciones.
# No se expone el saldo directamente, solo a través de métodos seguros como mostrar_saldo().

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular            # público
        self.__saldo = saldo_inicial      # privado

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: ${self.__saldo}")

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("Monto inválido")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes o monto inválido")

# Ejemplo de uso
cuenta = CuentaBancaria("Juan Perez", 1000)
cuenta.mostrar_saldo()  # Muestra el saldo inicial
cuenta.depositar(500)  # Deposita 500
cuenta.mostrar_saldo()  # Muestra el saldo después del depósito
cuenta.retirar(200)  # Retira 200
cuenta.mostrar_saldo()  # Muestra el saldo después del retiro
cuenta.retirar(1500)  # Intenta retirar más de lo que hay en la cuenta