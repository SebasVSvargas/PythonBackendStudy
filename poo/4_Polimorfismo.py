

class Perro:
    def hablar(self):
        return "Guau!"

class Gato:
    def hablar(self):
        return "Miau!"

# Polimorfismo en acción:
def hacer_hablar(animal):
    print(animal.hablar())

p = Perro()
g = Gato()

hacer_hablar(p)  # Guau!
hacer_hablar(g)  # Miau!

# 🔹 Aquí, hacer_hablar() acepta cualquier objeto que tenga un método hablar()


#otro ejemplo:

class Ave:    
    def volar(self):
        return "El ave vuela"
    
class Murcielago(Ave):
    def volar(self):
        return "El murciélago vuela de noche"
    
class Pinguino(Ave):
    def volar(self):
        return "El pingüino no vuela, pero nada muy bien"
    
def hacer_volar(ave):
    print(ave.volar())

a = Ave()
m = Murcielago()    
p = Pinguino()
hacer_volar(a)  # El ave vuela
hacer_volar(m)  # El murciélago vuela de noche
hacer_volar(p)  # El pingüino no vuela, pero nada muy bien
    
