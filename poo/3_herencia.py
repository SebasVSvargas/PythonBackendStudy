
# _______Herencia________

class Animal:
    especie = "Desconocida"

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def describir_especie(cls):
        print(f"Esta clase representa la especie: {cls.especie}")


class Perro(Animal):
    especie = "Canino"

class Gato(Animal):
    especie = "Felino"


Animal.describir_especie()  # Esta clase representa la especie: Desconocida
Perro.describir_especie()   # Esta clase representa la especie: Canino
Gato.describir_especie()    # Esta clase representa la especie: Felino

perro = Perro("Rex")

# 🔹 Aunque el método describir_especie() está definido en la clase base Animal, 
# cada subclase lo ejecuta con su propia versión del atributo especie, gracias al uso de cls.



# _______Herencia Múltiple________
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mostrar_marca(self):
        print(f"Marca del vehículo: {self.marca}")

class Electrico:
    def __init__(self, bateria):
        self.bateria = bateria

    def mostrar_bateria(self):
        print(f"Batería del vehículo eléctrico: {self.bateria} kWh")

class Coche(Vehiculo, Electrico):
    def __init__(self, marca, bateria):
        Vehiculo.__init__(self, marca)
        Electrico.__init__(self, bateria)

    def mostrar_info(self):
        self.mostrar_marca()
        self.mostrar_bateria()

# Ejemplo de uso
coche = Coche("Tesla", 75)
coche.mostrar_marca() # puede acceder al método de Vehiculo
coche.mostrar_bateria()  # puede acceder al método de Electrico
coche.mostrar_info()  # muestra información de ambos padres

# 🔹 En este ejemplo, Coche hereda de dos clases: Vehiculo y Electrico.



#uso de herencia con metodo base sin implementación
class AnimalBase:
    def hacer_sonido(self):
        pass
        # raise NotImplementedError("Subclases deben implementar este método")    

class Perro(AnimalBase):
    def hacer_sonido(self):
        return "Guau"
class Gato(AnimalBase):
    def hacer_sonido(self):
        return "Miau"
# Ejemplo de uso
perro = Perro() 
gato = Gato()
print(perro.hacer_sonido())  # Salida: Guau
print(gato.hacer_sonido())   # Salida: Miau
# 🔹 Aquí, AnimalBase define un método hacer_sonido() que no está implementado


# Uso de pass en herencia
class Animal():
    def __init__(self, sonido: str):
        self.sonido = sonido
    def hacer_sonido(self):
        return self.sonido 

class Perro(Animal):
    pass # no implementa hacer_sonido(), hereda de Animal

class Gato(Animal):
    pass

class PerroGato(Perro, Gato):
    def __init__(self, sonido_perro: str, sonido_gato: str):
        Perro.__init__(self, sonido_perro)
        Gato.__init__(self, sonido_gato)

    # def hacer_sonido(self):
    #     return f"{Perro.hacer_sonido(self)} y {Gato.hacer_sonido(self)}"

# Ejemplo de uso
perro = Perro("Guau")
gato = Gato("Miau")
print(perro.hacer_sonido())  # Salida: Guau
print(gato.hacer_sonido())   # Salida: Miau

perro_gato = PerroGato("guau", "miau")
print(perro_gato.hacer_sonido())


# herencia de clases que contienen metodos con el mismo nombre
class Persona:
    def saludo(self):
        print("Saludo como humano.")

class Maquina:
    def saludo(self):
        print("Saludo como máquina.")

class RobotAsistente(Persona, Maquina):
    pass

robo = RobotAsistente()
robo.saludo() # Imprime: Saludo como humano

print(RobotAsistente.__mro__)


# Ejemplo: Robot con herencia múltiple + uso de super()
class SentidoComun:
    def __init__(self):
        print("Inicializando sentido común...")

    def actuar(self):
        print("Evaluando el entorno antes de actuar.")

class LogicaProgramada:
    def __init__(self):
        print("Cargando lógica programada...")

    def actuar(self):
        print("Ejecutando instrucciones automatizadas.")

class RobotInteligente(SentidoComun, LogicaProgramada):
    def __init__(self):
        super().__init__()  # Solo llama a SentidoComun.__init__ por orden de MRO
        LogicaProgramada.__init__(self)  # Se llama explícitamente al segundo constructor
        print("Robot inteligente listo para operar.")

    def actuar(self):
        print("Combinando razonamiento humano y computacional:")
        super().actuar()  # Llama a SentidoComun.actuar() automáticamente
        LogicaProgramada.actuar(self)  # Llama explícitamente al otro método

# Ejemplo de uso
# sentido = SentidoComun()
# sentido.actuar()

# logica = LogicaProgramada()
# logica.actuar()

robot = RobotInteligente()
robot.actuar() 

# llamar al metodo actuar de la clase logica programada
LogicaProgramada.actuar(robot)  # Llama explícitamente al método de la clase LogicaProgramada