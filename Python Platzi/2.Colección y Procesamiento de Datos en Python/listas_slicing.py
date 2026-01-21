a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))
c = a[:] # crea una copia de la lista
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(a)
print(b)
print(c)

#tambien se puede copiar una lista usando el metodo copy
lista1 = [1,2,3,4,5]
lista2 = lista1.copy()
lista2.append( 6 )

print( lista1 )
print( lista2 )