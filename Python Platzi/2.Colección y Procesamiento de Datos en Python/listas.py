# to_do = ["Dirigirnos al hotel",
#          "Ir a almorzar",
#          "Visitar un museo",
#          "Volver al hotel"]
# print(to_do)
# numbers = [1,2,3,4, "cinco"]
# print(type(numbers))
# mix = ["uno", 2, 3.14, True, [1,2,3]]
# print("Mix datos",mix)
# print(len(mix))
# print("Primer elemento", mix[0])
# print("Segundo elemento", mix[1])
# print("Ultimo elemento:", mix[-1])
# string = "Hola mundo"
# print("Primer elemento", string[0])
# print("Segundo elemento", string[1])
# print("Ultimo elemento:", string[-1])
# print(mix[2:-2])
# print(mix)
# mix.append(False)
# print(mix)
# mix.append(["a","b"])
# print(mix)
# mix.insert(1,["a","b"])
# print(mix)
# print(mix.index(["a","b"]))
# numbers = [1,2,100.01,90.45,3,4, 5]
# print(numbers)
# print("Mayor:",max(numbers))
# print("Menor:",min(numbers))
# del numbers[-1]
# print(numbers)
# del numbers[:2]
# print(numbers)
# del numbers
# print(numbers)

# Creación de listas
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]

print("Lista vacía:", lista_vacia)
print("Lista de números:", lista_numeros)
print("Lista mixta:", lista_mixta)

# Acceder a elementos
print("\nAcceso a elementos")
print("Primer elemento:", lista_numeros[0])
print("Último elemento:", lista_numeros[-1])

# Modificar elementos
print("\nModificar elementos")
lista_numeros[0] = 10
print("Lista de números modificada:", lista_numeros)

# Agregar y eliminar elementos
print("\nAgregar y eliminar elementos")
lista_numeros.append(6)
print("Lista después de append:", lista_numeros)
lista_numeros.insert(2, 99)
print("Lista después de insert:", lista_numeros)
lista_numeros.remove(99)
print("Lista después de remove:", lista_numeros)
ultimo = lista_numeros.pop()
print("Elemento eliminado con pop:", ultimo)
print("Lista después de pop:", lista_numeros)
elemento = lista_numeros.pop(1)
print("Elemento eliminado en la posición 1:", elemento)
print("Lista después de eliminar en la posición 1:", lista_numeros)

# Operaciones básicas
print("\nOperaciones básicas")
lista_concatenada = lista_numeros + lista_mixta
print("Lista concatenada:", lista_concatenada)
lista_repetida = lista_numeros * 2
print("Lista repetida:", lista_repetida)
print("¿Está 3 en la lista?", 3 in lista_numeros)
print("Longitud de la lista:", len(lista_numeros))

# Iteración sobre los elementos de una lista
print("\nIteración sobre elementos de la lista")
for elemento in lista_numeros:
    print(elemento)

# Salida final
print("\nGracias por utilizar el programa de listas. ¡Hasta la próxima!")

# Creación de listas

lista_vacia = []

lista_numeros = [1, 2, 3, 4, 5]

lista_mixta = [1, "dos", 3.0, True]



print("Lista vacía:", lista_vacia)

print("Lista de números:", lista_numeros)

print("Lista mixta:", lista_mixta)



# Acceder a elementos

print("\nAcceso a elementos")

print("Primer elemento:", lista_numeros[0])

print("Último elemento:", lista_numeros[-1])



# Modificar elementos

print("\nModificar elementos")

lista_numeros[0] = 10

print("Lista de números modificada:", lista_numeros)



# Agregar y eliminar elementos

print("\nAgregar y eliminar elementos")

lista_numeros.append(6)

print("Lista después de append:", lista_numeros)

lista_numeros.insert(2, 99)

print("Lista después de insert:", lista_numeros)

lista_numeros.remove(99)

print("Lista después de remove:", lista_numeros)

ultimo = lista_numeros.pop()

print("Elemento eliminado con pop:", ultimo)

print("Lista después de pop:", lista_numeros)

elemento = lista_numeros.pop(1)

print("Elemento eliminado en la posición 1:", elemento)

print("Lista después de eliminar en la posición 1:", lista_numeros)



# Operaciones básicas

print("\nOperaciones básicas")

lista_concatenada = lista_numeros + lista_mixta

print("Lista concatenada:", lista_concatenada)

lista_repetida = lista_numeros * 2

print("Lista repetida:", lista_repetida)

print("¿Está 3 en la lista?", 3 in lista_numeros)

print("Longitud de la lista:", len(lista_numeros))



# Iteración sobre los elementos de una lista

print("\nIteración sobre elementos de la lista")

for elemento in lista_numeros: 
    print(elemento)