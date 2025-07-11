class Singleton:
    _instance = None # El guion bajo al principio indica que es un atributo privado de la clase

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    


class MySingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MySingleton, cls).__new__(cls)


Singleton1 = Singleton()
Singleton2 = Singleton()
print(Singleton1 is Singleton2)  # True, ambas variables apuntan a la misma instancia

MySingleton1 = MySingleton()
MySingleton2 = MySingleton()
print(MySingleton1 is MySingleton2)  # True, ambas variables apuntan a la misma instancia


# singleton con campos

class SingletonWithFields:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonWithFields, cls).__new__(cls)
            cls._instance.field1 = args[0] if args else None
            cls._instance.field2 = kwargs.get('field2', None)
        return cls._instance
    
singleton_with_fields1 = SingletonWithFields("value1", field2="value2")
singleton_with_fields2 = SingletonWithFields("value3", field2="value4") # este no cambia los valores porque ya existe la instancia

print(singleton_with_fields1 is singleton_with_fields2)  # True, ambas variables apuntan a la misma instancia
print(singleton_with_fields1.field1)  # value1, el primer valor asignado
print(singleton_with_fields1.field2)  # value2, el primer valor asignado
