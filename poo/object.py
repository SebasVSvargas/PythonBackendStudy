from abc import ABC, abstractmethod

class People:
    class_name = "People" # es un campo de clase que puede ser accedido por todas las instancias

    def __init__(self, name: str, age: int):
        self.name = name # atributo público, se puede acceder directamente desde fuera de la clase
        self.__age = age # atributo privado, no se puede acceder directamente desde fuera de la clase

    def hi(self):
        #print("Hello, I am a person! My name is", self.name)
        #print("Hello, " + self.name)
        print(f"Hello, {self.name} nice to meet you!")

    def get_age(self):  #Método para obtener la edad ya que es privada
        return self.__age

    def __some(self): #Método privado, no se puede acceder desde fuera de la clase
        print("algo privado")

    @staticmethod
    def static_method_example(): #no necesita un self, no es una instancia de la clase
        """This is a static method that can be called without an instance."""

        print("This is a static method, it can be called without an instance.")

    @classmethod
    def class_method_example(cls):
        """This is a class method that can be called on the class itself."""

        print(f"This is a class method, it can be called on the class {cls.class_name} itself.")
        cls.class_name = "Toronbolo"  # Modifica el campo de clase


Sebas = People("Sebas",28)
Daniel = People("Daniel",22)
Sebas.hi()
# People.hi(self=Sebas)  # Llamada al método de instancia

print("Campo Class name:", Sebas.class_name)
print("Campo Class name:", People.class_name)

Sebas.class_method_example() # acá se modifica el campo de clase así que ahora desde donde sea que se
                             # llame a class_name va a tener un valor diferente al original
print("Campo Class name:", Daniel.class_name)
print("Campo Class name:", People.class_name)

Sebas.static_method_example()  # Llamada al método estático
People.static_method_example()  # También se puede llamar directamente desde la clase

People.class_method_example()  # Llamada al método de clase

#acá se genera un error porque no se puede acceder al atributo privado __age directamente
# print(Sebas.__age)




class Procesador(ABC):

    @abstractmethod
    def procesar(self, *args, **kwargs):
        pass  # Método abstracto que debe ser implementado por las subclases


class ProcesadorTexto(Procesador):

    def procesar(self,*args, **kwargs):
        print("Procesando texto...")
        for texto in args:
            print(f"texto: {texto}")
        if "mayusculas" in kwargs and kwargs['mayusculas']:
            print("Transformando a Mayusculas")
            for texto in args:
                print(texto.upper())    
        
# Subclase que procesa imágenes
class ProcesadorImagen(Procesador):
    def procesar(self, *args, **kwargs):
        print("Procesando imágenes...")
        for imagen in args:
            print(f"Imagen recibida: {imagen}")
        if 'formato' in kwargs:
            print(f"Guardando en formato: {kwargs['formato']}")


# Uso polimórfico
def ejecutar_procesamiento(procesador: Procesador, *args, **kwargs):
    procesador.procesar(*args, **kwargs)

texto_proc = ProcesadorTexto()
imagen_proc = ProcesadorImagen()

ejecutar_procesamiento(texto_proc, "Hola mundo", "Python es genial", mayusculas=True)
print("\n" + "-"*40 + "\n")
# ejecutar_procesamiento(imagen_proc, "imagen1","imagen2","imagen3", formato=".jpg")
ejecutar_procesamiento(imagen_proc, "foto1.png", "foto2.jpg", formato="PNG")