import http.client
from abc import ABC, abstractmethod

class HttpRequest(ABC):
    """Interfaz del 'Producto' en el patrón Factory Method.
    Define la operación que deberán implementar las solicitudes HTTP concretas.
    """
    @abstractmethod
    def request(self, resource_id: int) -> str:
        """Realiza la solicitud y devuelve el cuerpo como texto."""
        pass

class HttpGet(HttpRequest):
    """Implementación concreta de una solicitud HTTP GET."""
    def __init__(self, domain:str, path:str):
        # Guarda el dominio y la ruta base (sin slash inicial).
        # Ej.: domain="jsonplaceholder.typicode.com", path="posts"
        self.__domain = domain
        self.__path = path

    def request(self, resource_id:int) -> str:
        """Realiza GET a: https://{domain}/{path}/{resource_id} y devuelve el cuerpo como str."""
        connection = http.client.HTTPSConnection(self.__domain, timeout=10)
        try:
            # Construimos la ruta completa. Importante: usar "posts" (plural) en JSONPlaceholder.
            full_path = f"/{self.__path}/{resource_id}"
            connection.request("GET", full_path)
            response = connection.getresponse()

            if response.status == 200:
                data = response.read()
                return data.decode("utf-8")
            else:
                # Mensaje claro para depurar rápidamente.
                return f"Error en la solicitud: {response.status} {response.reason} ({full_path})"
        finally:
            # Asegura cierre de la conexión incluso si hay errores.
            connection.close()

class HttpRequestFactory(ABC):
    """Creador base del patrón Factory Method. Encapsula dominio y ruta."""
    def __init__(self, domain:str, path:str):
        self._domain = domain
        self._path = path

    @abstractmethod
    def create(self) -> HttpRequest:
        """Devuelve una instancia concreta de HttpRequest."""
        pass

class HttpGetFactory(HttpRequestFactory):
    """Creador concreto que fabrica solicitudes GET."""
    def create(self) -> HttpRequest:
        return HttpGet(self._domain, self._path)

# Create the factory
http_get_factory = HttpGetFactory("jsonplaceholder.typicode.com", "posts")

# Create the object from the factory y ejecuta la solicitud GET a /posts/7
http_get = http_get_factory.create()
http_get2 = http_get_factory.create()


print(f"{http_get.request(7)}")
print(f"{http_get2.request(16)}")
