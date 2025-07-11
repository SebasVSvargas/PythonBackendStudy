#Diferencias entre métodos de instancia, de clase y estáticos en Python:

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}."
    
# 🔸 Aquí, saludar() usa self para acceder al atributo nombre de la instancia.


class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
# 🔸 Aquí, sumar() no usa ni self ni cls, por lo que es independiente del estado de la clase o sus objetos.
    

class Usuario:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.contador += 1

    @classmethod
    def obtener_total_usuarios(cls):
        return cls.contador
    
# 🔸 El método obtener_total_usuarios() usa cls.contador para acceder al estado compartido por la clase, 
# no por una instancia.