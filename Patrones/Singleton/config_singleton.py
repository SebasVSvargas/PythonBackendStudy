
import json
import os

print("Directorio actual:", os.getcwd())

file_path = os.path.join(os.path.dirname(__file__), "config.json")

class ConfigSingleton:
    _instance = None

    def __new__(cls, file_name = file_path):
        if not cls._instance:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            cls._instance.__load_json(file_name)
        return cls._instance

    def __load_json(self, file_name: str):
        '''
        Se encarga de cargar el archivo especificado 
        para guardarlo en una variable y poder trabajar con este

        file_name: ruta del archivo.
        '''
        try:
            with open(file_name, "r") as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = None
            print("Archivo no encontrado")
        except json.JSONDecodeError:
            self.config = None
            print("Formato no valido en archivo Json")

    def get(self, key):
        '''
        Obtiene el valor de la clave especificada en el archivo Json
        key: clave del archivo Json.
        '''
        return self.config.get(key)


config1 = ConfigSingleton()
print(config1.get("version"))  # Imprime la versión del config.json
print(config1.get("name"))     # Imprime el nombre del config.json

config2 = ConfigSingleton()
print(config1 is config2)  # Verifica si ambas instancias son la misma