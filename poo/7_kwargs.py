
def show(**kwargs):
    """
    Función que muestra los argumentos recibidos.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Ejemplo de uso
show(nombre="Juan", edad=30, ciudad="Madrid")
# 🔹 Aquí, show() acepta un número variable de argumentos con nombre (kwargs).



#Otro ejemplo más complejo:
def crear_usuario(**datos):
    """
    Crea un usuario con los datos proporcionados.
    
    :param datos: Información del usuario.
    :return: Diccionario con los datos del usuario.
    """
    usuario = {}
    for clave, valor in datos.items():
        usuario[clave] = valor # acá se está creando un diccionario con los datos del usuario
    return usuario

# Ejemplo de uso
usuario1 = crear_usuario(nombre="Ana", edad=25, email="svas")

print(usuario1)  # {'nombre': 'Ana', 'edad': 25, 'email': 'svas'}