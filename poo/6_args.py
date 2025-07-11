
# el * permite recibir un número variable de argumentos
# se pueden pasar números, cadenas, listas, tuplas, etc.

def add(*args):
    """
    Suma todos los números pasados como argumentos.
    
    :param args: Números a sumar.
    :return: Suma de los números.
    """
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            continue
            #raise ValueError(f"Argumento no numérico: {num}")
        
    return total
    # return sum(args)

res1 = add(1, 2, 3, 4, 5)
res2 = add(10, 20, 30)
res3 = add(1.5, 2.5, 3.5)
res4 = add(1, "dos", 3.0, [4], (5,))

print(f"Resultado 1: {res1}")  # Resultado 1: 15
print(f"Resultado 2: {res2}")  # Resultado 2: 60
print(f"Resultado 3: {res3}")  # Resultado 3: 7.5
print(f"Resultado 4: {res4}")  # Resultado 4: 4.0 (solo suma los números válidos)