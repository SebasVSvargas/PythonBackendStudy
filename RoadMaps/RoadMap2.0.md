# Roadmap Definitivo para Backend Developer Python

## Fase 1: Fundamentos de Python


### Sintaxis y Tipos de Datos

* **Concepto Clave y Relevancia Profesional:** Es el vocabulario y la gramática de Python. Sin esto, no puedes comunicarle al ordenador la lógica de negocio más básica. Las empresas necesitan que escribas código claro, eficiente y libre de errores sintácticos obvios desde el primer día.
* **Objetivos de Aprendizaje Concretos:**
    * Implementar un script que utilice al menos tres tipos de bucles (for, for anidado, while) para procesar una lista de diccionarios.
    * Escribir funciones que reciban diferentes tipos de datos y usen operadores lógicos para devolver un resultado.
    * Refactorizar un bloque de `if/elif/else` anidado en una versión más legible, posiblemente usando diccionarios.
* **Temas a Dominar:**
    * Variables y asignación.
    * Tipos de datos primitivos: `int`, `float`, `str`, `bool`, `None`.
    * Operadores: aritméticos, de comparación, lógicos.
    * Control de flujo: `if`, `elif`, `else`.
    * Bucles: `for`, `while`.
    * Palabras clave de control de bucles: `break`, `continue`, `pass`.
    * F-strings para formateo de cadenas.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Usa siempre f-strings (`f"Hola, {variable}"`) para formatear cadenas. Es más rápido y legible.
    * **Error Común:** Comparar un booleano con `== True` o `== False`. Es redundante. Simplemente escribe `if mi_variable:` o `if not mi_variable:`.
* **Mini-Proyecto:** Escribe un script de "Adivina el número". El programa elige un número aleatorio (1-100) y el usuario tiene 10 intentos para adivinarlo, recibiendo pistas de "más alto" o "más bajo".

### Estructuras de Datos a fondo

* **Concepto Clave y Relevancia Profesional:** Son las herramientas para organizar datos eficientemente. La elección incorrecta puede degradar catastróficamente el rendimiento de una aplicación a escala.
* **Objetivos de Aprendizaje Concretos:**
    * Resolver un problema usando un `set` para encontrar elementos únicos o comunes entre dos listas.
    * Implementar una función que transforme una lista de tuplas en un diccionario usando una comprensión de diccionario.
    * Explicar la diferencia de rendimiento entre buscar un elemento en una lista y en un diccionario/set.
* **Temas a Dominar:**
    * **Listas:** Métodos (`append`, `pop`, `sort`), slicing, mutabilidad.
    * **Diccionarios:** Claves y valores, métodos (`get`, `keys`, `items`), manejo de `KeyError`.
    * **Tuplas:** Inmutabilidad y casos de uso.
    * **Sets:** Operaciones de conjuntos y casos de uso (eliminar duplicados, pruebas de membresía rápidas).
    * **Comprensiones:** `List comprehensions` y `dict comprehensions`.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Utiliza `diccionario.get('clave', valor_por_defecto)` para evitar `KeyError` cuando no estás seguro de si una clave existe.
    * **Error Común:** Modificar una lista mientras se itera sobre ella. Si es necesario, itera sobre una copia: `for item in mi_lista[:]:`.
* **Mini-Proyecto:** Crea una función que reciba un texto y devuelva un diccionario con las 10 palabras más frecuentes y su conteo.

### Programación Orientada a Objetos (POO)

* **Concepto Clave y Relevancia Profesional:** POO es el paradigma para estructurar código en objetos reutilizables. Es la base de frameworks como Django y fundamental para construir sistemas complejos y mantenibles.
* **Objetivos de Aprendizaje Concretos:**
    * Implementar una clase base `Vehiculo` y dos clases derivadas (`Coche`, `Bicicleta`) que hereden de ella, demostrando polimorfismo.
    * Crear una clase con atributos de instancia, un método de clase y un método estático.
    * Implementar los métodos mágicos `__str__` y `__repr__` y explicar la diferencia.
* **Temas a Dominar:**
    * Clases y objetos.
    * Atributos de instancia vs. de clase.
    * Métodos: de instancia (`self`), de clase (`@classmethod`), estáticos (`@staticmethod`).
    * Pilares: Encapsulamiento, Herencia, Polimorfismo.
    * Métodos Mágicos: `__init__`, `__str__`, `__repr__`, `__eq__`.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Sigue el Principio de Responsabilidad Única. Cada clase debe tener una única responsabilidad bien definida.
    * **Error Común:** Usar un tipo mutable (lista, dict) como valor por defecto en la firma de un método. El valor correcto es `None` y se inicializa dentro del método.
* **Mini-Proyecto:** Modela un sistema simple de una biblioteca con clases para `Libro`, `Autor` y `Biblioteca`.

### Manejo de Errores y Excepciones

* **Concepto Clave y Relevancia Profesional:** Es el mecanismo para manejar errores sin que el programa se caiga. Un backend robusto anticipa fallos, los maneja elegantemente y devuelve respuestas apropiadas.
* **Objetivos de Aprendizaje Concretos:**
    * Escribir una función que lea un archivo y use `try/except` para `FileNotFoundError` y `finally` para asegurar que el archivo se cierre.
    * Crear una excepción personalizada (ej. `SaldoInsuficienteError`) y lanzarla (`raise`) en el contexto apropiado.
* **Temas a Dominar:**
    * Diferencia entre error de sintaxis y excepción.
    * Bloques `try`, `except Exception as e`, `else` y `finally`.
    * Manejar excepciones específicas (`ValueError`, `TypeError`).
    * La palabra clave `raise`.
    * Creación de excepciones personalizadas.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Sé específico en tus bloques `except`. Evita `except Exception:` genérico que pueda ocultar errores inesperados.
    * **Error Común:** Usar excepciones para control de flujo normal. Si puedes usar un `if`, es casi siempre preferible.
* **Mini-Proyecto:** Crea una función que reciba un diccionario y una clave. Debe manejar `KeyError` (logueando un warning) y `TypeError` (lanzando una excepción personalizada si el valor no es un número).

## Fase 2: Entornos Virtuales y Gestión de Proyectos con Poetry

*Aquí es donde pasas de escribir scripts a construir aplicaciones profesionales. Es un paso no negociable en la industria.*

### Poetry: Gestión Moderna de Dependencias

* **Concepto Clave y Relevancia Profesional:** Poetry gestiona las dependencias de tu proyecto y crea entornos aislados. Resuelve el "en mi máquina funciona" al asegurar que todos usen exactamente las mismas versiones de las librerías.
* **Objetivos de Aprendizaje Concretos:**
    * Inicializar un proyecto con `poetry new`.
    * Añadir dependencias de producción (`fastapi`) y de desarrollo (`pytest`) con `poetry add`.
    * Explicar el propósito del archivo `poetry.lock`.
    * Ejecutar un script con `poetry run`.
* **Temas a Dominar:**
    * El problema que resuelven los entornos virtuales.
    * Comandos esenciales: `new`, `init`, `install`, `add`, `remove`, `run`, `shell`, `update`.
    * El archivo `pyproject.toml` y su estructura.
    * El archivo `poetry.lock`: la única fuente de la verdad para las versiones.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Siempre haz "commit" de tu archivo `poetry.lock` a Git. Esto garantiza builds reproducibles.
    * **Error Común:** Instalar dependencias con `pip` dentro de un entorno gestionado por Poetry. Usa siempre `poetry add`.
* **Mini-Proyecto:** Crea un proyecto con Poetry, añade `requests`, y escribe un script que consuma la API de `pokeapi.co` para mostrar el nombre de un Pokémon.

## Fase 3: APIs de Alto Rendimiento con FastAPI y Pydantic

*Este es el núcleo del stack moderno. Dominar FastAPI te posiciona en la vanguardia del desarrollo backend con Python.*

### **(NUEVO) Estructura de Proyectos Escalables**

* **Concepto Clave y Relevancia Profesional:** A medida que una aplicación crece, mantener todo en un solo archivo es insostenible. Aprender a organizar tu código en módulos con responsabilidades claras desde el principio es fundamental para la mantenibilidad y el trabajo en equipo.
* **Objetivos de Aprendizaje Concretos:**
    * Refactorizar una API simple de un solo archivo a una estructura de múltiples archivos/carpetas.
    * Crear y utilizar un `APIRouter` para agrupar endpoints relacionados.
    * Explicar el flujo de una petición a través de las capas de la aplicación (router -> servicio -> modelo).
* **Temas a Dominar:**
    * **Separación de Responsabilidades:** Organizar el código en carpetas/módulos (`routers`, `services`, `models`, `core`).
    * **`APIRouter`:** Cómo usar los routers para dividir los endpoints en archivos lógicos (ej. `routers/users.py`, `routers/tasks.py`) e incluirlos en la aplicación principal.
    * **Capas de Lógica:** Entender el patrón donde los *routers* manejan las peticiones HTTP, los *servicios* contienen la lógica de negocio y los *modelos* definen las estructuras de datos.
* **Mini-Proyecto:** Toma la API de "lista de tareas" que construirás en las siguientes secciones y organízala desde el principio usando `APIRouter` para los endpoints de tareas y separando los modelos de Pydantic en un archivo `schemas.py` o `models.py`.

### Importancia de FastAPI

* **Concepto Clave y Relevancia Profesional:** FastAPI es un framework web de alto rendimiento para construir APIs. Las empresas lo adoptan por su increíble velocidad, la validación de datos automática y la reducción drástica en el tiempo de desarrollo.
* **Objetivos de Aprendizaje Concretos:**
    * Explicar qué es ASGI y cómo contribuye al rendimiento de FastAPI.
    * **(RECOMENDACIÓN INTEGRADA)** Explicar qué es el bucle de eventos (Event Loop) y por qué una llamada síncrona bloqueante (ej. `requests.get()`) puede degradar el rendimiento de toda la aplicación.
    * Observar cómo los *type hints* se convierten en validación de datos y documentación automática.
* **Temas a Dominar:**
    * ASGI vs WSGI (asíncrono vs síncrono).
    * Starlette y Pydantic: Las bases de FastAPI.
    * Declaraciones de tipo (Type Hints) y su impacto.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Aprovecha al máximo los type hints en todo tu código, no solo en los modelos.
    * **Error Común:** Mezclar código síncrono bloqueante en un endpoint `async def`. Usa librerías asíncronas (como `httpx`) para operaciones de I/O.
* **Mini-Proyecto:** Instala `fastapi` y `uvicorn` y lanza el "Hello World" de FastAPI.

### Path Operations

* **Concepto Clave y Relevancia Profesional:** Son las funciones que se ejecutan cuando un cliente hace una petición a una URL y método HTTP específicos. Es la forma fundamental de definir la funcionalidad de tu API.
* **Objetivos de Aprendizaje Concretos:**
    * Crear un endpoint GET con parámetros de ruta (ej. `/items/{item_id}`).
    * Crear un endpoint GET con parámetros de consulta opcionales (ej. `/search?q=query`).
    * Implementar un endpoint POST que reciba y valide un cuerpo JSON.
* **Temas a Dominar:**
    * Decoradores: `@app.get()`, `@app.post()`, etc.
    * Parámetros de Ruta, de Consulta (Query) y Cuerpo de la Petición (Body).
    * Códigos de estado HTTP.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Usa sustantivos en plural para tus rutas de colección (`/users`) y un identificador para el recurso específico (`/users/{user_id}`).
    * **Error Común:** Poner un parámetro de ruta opcional. Los parámetros de ruta no pueden ser opcionales; los de consulta sí.
* **Mini-Proyecto:** Crea una API de "lista de tareas" en memoria con endpoints para obtener todas las tareas, añadir una nueva y obtener una específica.

### Pydantic para Validación de Datos

* **Concepto Clave y Relevancia Profesional:** Pydantic usa type hints para validar, serializar y deserializar datos de forma automática. Elimina una enorme cantidad de código de validación manual y previene incontables bugs.
* **Objetivos de Aprendizaje Concretos:**
    * Definir un modelo `BaseModel` de Pydantic para los datos de entrada de un endpoint.
    * Utilizar tipos de datos avanzados de Pydantic (`EmailStr`, `HttpUrl`) y validaciones con `Field`.
    * Interpretar los errores de validación que FastAPI devuelve automáticamente.
* **Temas a Dominar:**
    * Herencia de `pydantic.BaseModel`.
    * Tipos básicos y complejos (`List`, `Dict`, `Optional`).
    * Validadores personalizados con `@validator`.
    * Control de la salida con `response_model`.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Crea modelos específicos para la entrada (`ItemCreate`) y la salida (`ItemRead`). El de salida puede tener campos que el cliente no debe enviar (`id`, `created_at`).
    * **Error Común:** Devolver directamente un modelo de la base de datos (ej. SQLAlchemy) sin usar un `response_model`, exponiendo campos que no deberían ser públicos.
* **Mini-Proyecto:** En tu API de tareas, reemplaza los diccionarios con modelos de Pydantic: `TaskCreate` para el POST y `TaskRead` (con `id`) para los GET.

### Dependency Injection

* **Concepto Clave y Relevancia Profesional:** Es un patrón donde las dependencias que una función necesita son "inyectadas" desde fuera. En FastAPI, permite una increíble reutilización de código para lógica como conexiones a BD, autenticación o paginación.
* **Objetivos de Aprendizaje Concretos:**
    * Crear una función "dependable" para parámetros comunes (paginación) y usarla en múltiples endpoints.
    * Implementar una dependencia para obtener una sesión de base de datos y asegurar que se cierre correctamente.
* **Temas a Dominar:**
    * La función `Depends` de FastAPI.
    * Dependencias como funciones y clases.
    * Dependencias con `yield` para código de limpieza (ej. cerrar conexión a BD).
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Mantén tus dependencias pequeñas y enfocadas en una sola tarea (obtener la sesión de BD, obtener el usuario actual, etc.).
    * **Error Común:** Poner lógica de negocio compleja dentro de una dependencia. Las dependencias son para "plomería" (obtener cosas, verificar permisos), no para la lógica central.
* **Mini-Proyecto:** Crea una dependencia `async def get_db_session()` (puede ser una función falsa por ahora) e inyéctala en tus endpoints de la API de tareas.

### Documentación Automática (Swagger/ReDoc)

* **Concepto Clave y Relevancia Profesional:** FastAPI genera automáticamente documentación interactiva de tu API. Esto ahorra incontables horas, sirve como contrato para el frontend y permite probar los endpoints desde el navegador.
* **Objetivos de Aprendizaje Concretos:**
    * Navegar a los endpoints `/docs` (Swagger UI) y `/redoc`.
    * Utilizar la interfaz de Swagger para probar un endpoint POST.
    * Añadir metadatos como `title`, `description` y `tags` para enriquecer la documentación.
* **Temas a Dominar:**
    * OpenAPI: El estándar detrás de la documentación.
    * Swagger UI (`/docs`) y ReDoc (`/redoc`).
    * Añadir metadatos (`summary`, `description`, `tags`) a los decoradores.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Sé prolijo con las descripciones y ejemplos en tus modelos (`Field(..., example="John Doe")`). Un buen `description` ahorra mucho tiempo.
    * **Error Común:** No documentar los posibles errores (ej. 404, 403) que un endpoint puede devolver. Usa el parámetro `responses`.
* **Mini-Proyecto:** En tu API de tareas, añade `tags`, descripciones claras a cada endpoint y a los campos de tus modelos. Explora la documentación generada.

## **(NUEVA FASE) Fase 4: Testing Automatizado de APIs**

*El código que no se prueba, está roto por definición. Aprender a escribir pruebas automatizadas es la diferencia entre un amateur y un ingeniero profesional. El testing es tu red de seguridad para refactorizar y añadir funcionalidades con confianza.*

### **Testing con Pytest y TestClient**

* **Concepto Clave y Relevancia Profesional:** El testing automatizado verifica que tu código hace lo que se supone que debe hacer, ahora y en el futuro. Pytest es el estándar de facto para el testing en Python por su sintaxis simple y su potente sistema de fixtures. FastAPI proporciona un `TestClient` que te permite llamar a tu API dentro de las pruebas sin necesidad de un servidor real.
* **Objetivos de Aprendizaje Concretos:**
    * Escribir una prueba unitaria simple para una función de lógica de negocio.
    * Configurar `pytest` y el `TestClient` de FastAPI para escribir pruebas de integración para tus endpoints.
    * Escribir una prueba para un endpoint `POST /tasks`, enviando datos de prueba y verificando que el código de estado sea `201` y que los datos devueltos sean correctos.
    * Escribir una prueba para un endpoint que requiere autenticación, pasando un token de prueba en las cabeceras.
    * Implementar una estrategia para usar una base de datos de prueba separada para tus tests.
* **Temas a Dominar:**
    * Fundamentos de `pytest`: Funciones de test (`test_*`), `asserts`.
    * Fixtures de `pytest`: Qué son y cómo usarlas para configurar el estado de una prueba (ej. crear un cliente de prueba, una sesión de BD).
    * Uso del `TestClient`: `client.get()`, `client.post()`, `client.put()`, `client.delete()`.
    * Verificación de respuestas: `response.status_code`, `response.json()`.
    * Mocking y Patching: Cómo simular dependencias externas o funciones para aislar el código bajo prueba.
    * Estrategias de Base de Datos de Prueba: Uso de una BD en memoria (SQLite) para tests rápidos o una BD de prueba temporal en PostgreSQL.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Tus pruebas deben ser independientes y no depender del orden de ejecución. Usa fixtures para crear los recursos necesarios para cada prueba y limpiarlos después.
    * **Error Común:** Escribir pruebas que dependen de servicios externos (APIs de terceros, etc.). Esto hace que tus pruebas sean lentas y poco fiables. Aprende a "mockear" esas llamadas para que tus pruebas solo verifiquen tu propio código.
* **Mini-Proyecto:** Para tu API de lista de tareas, escribe un conjunto de pruebas que cubra todo el CRUD. Asegúrate de probar tanto los casos de éxito (crear una tarea correctamente) como los casos de error (intentar obtener una tarea que no existe y verificar que recibes un 404).

## Fase 5: Bases de Datos con SQLModel y PostgreSQL

*Aquí es donde tu API cobra vida, persistiendo datos más allá del reinicio del servidor.*

### SQLModel: El ORM para FastAPI

* **Concepto Clave y Relevancia Profesional:** SQLModel es un ORM que combina Pydantic y SQLAlchemy, permitiéndote definir tus modelos de base de datos y API en una única clase. Esto reduce drásticamente la duplicación de código (DRY) y minimiza errores.
* **Objetivos de Aprendizaje Concretos:**
    * Definir un modelo de tabla de BD usando una clase que herede de `SQLModel`.
    * Crear el "motor" (engine) para conectar la aplicación a PostgreSQL.
    * Implementar las operaciones CRUD de forma asíncrona usando sesiones.
* **Temas a Dominar:**
    * Definición de modelos y campos (`Field(primary_key=True)`).
    * Creación del `engine` (síncrono y asíncrono).
    * El patrón de Sesión como unidad de trabajo transaccional.
    * Consultas con `select()` y ejecución con `session.exec()`.
    * Operaciones CRUD: `add()`, `get()`, `delete()`, `commit()`, `refresh()`.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Abstrae la lógica de la base de datos en una capa de "repositorio" o "servicio". Tus endpoints no deben contener código de SQLAlchemy; deben llamar a funciones como `crud.get_user()`.
    * **Error Común:** Olvidar hacer `session.commit()` al final de una transacción que modifica datos.
* **Mini-Proyecto:** Refactoriza tu API de tareas para usar SQLModel y PostgreSQL. Implementa los endpoints CRUD para que interactúen con la base de datos real. Usa `docker-compose` para levantar PostgreSQL.

### PostgreSQL (Relacional)

* **Concepto Clave y Relevancia Profesional:** PostgreSQL es una de las bases de datos relacionales de código abierto más potentes y utilizadas. Su soporte para transacciones ACID la hace ideal para aplicaciones donde la integridad de los datos es primordial.
* **Objetivos de Aprendizaje Concretos:**
    * Escribir consultas SQL básicas (SELECT, JOIN, INSERT, UPDATE) directamente en un cliente de BD.
    * Explicar qué significa cada letra en ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad).
    * Inicializar y ejecutar una migración de base de datos usando Alembic.
* **Temas a Dominar:**
    * Lenguaje SQL fundamental: `SELECT`, `WHERE`, `JOIN`, etc.
    * Comandos DML (`INSERT`, `UPDATE`, `DELETE`) y DDL (`CREATE TABLE`).
    * Claves primarias y foráneas.
    * Índices y su impacto en el rendimiento.
    * Migraciones de esquema con Alembic (`revision`, `upgrade`).
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Nunca construyas consultas SQL concatenando strings. Siempre usa los mecanismos de parametrización de tu librería para prevenir inyección de SQL.
    * **Error Común:** No poner índices en las columnas que se usan frecuentemente en cláusulas `WHERE` o para `JOINs`.
* **Mini-Proyecto:** Conecta un cliente de BD a tu PostgreSQL. Examina la tabla `Task` creada por Alembic e intenta insertar y leer datos usando SQL puro.

### Redis (NoSQL - Caché)

* **Concepto Clave y Relevancia Profesional:** Redis es una base de datos en memoria extremadamente rápida, usada comúnmente como caché para reducir la carga sobre la base de datos principal y acelerar drásticamente los tiempos de respuesta.
* **Objetivos de Aprendizaje Concretos:**
    * Implementar una estrategia de caché "cache-aside" para un endpoint GET.
    * Invalidar (eliminar) la clave de caché cuando un endpoint `PUT` o `DELETE` modifica los datos.
    * Configurar un tiempo de expiración (TTL) en las claves de Redis.
* **Temas a Dominar:**
    * Comandos básicos de Redis: `SET`, `GET`, `DEL`, `EXPIRE`.
    * Patrones de caché.
    * Uso de una librería cliente de Redis para Python.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** No intentes cachear todo. Identifica las consultas más lentas y frecuentes; esos son los candidatos perfectos para el caché.
    * **Error Común:** Olvidar invalidar el caché. Si actualizas un dato en PostgreSQL pero no en Redis, tu API servirá datos obsoletos.
* **Mini-Proyecto:** Añade Redis a tu `docker-compose.yml`. Modifica el endpoint `GET /tasks/{task_id}` para que primero busque en Redis y, si no encuentra nada, consulte PostgreSQL y guarde el resultado en Redis con un TTL.

## Fase 6: Seguridad en APIs

*Una API sin seguridad es una puerta abierta. Esta fase es crítica para ser un desarrollador responsable.*

### Autenticación y Autorización con JWT

* **Concepto Clave y Relevancia Profesional:** JWT (JSON Web Tokens) es el estándar para la autenticación y autorización de forma segura y sin estado en APIs. El flujo OAuth2 es el estándar de la industria para obtener estos tokens.
* **Objetivos de Aprendizaje Concretos:**
    * Implementar un endpoint `/token` que devuelva un `access_token` JWT.
    * Crear una dependencia de seguridad que extraiga y valide el token de la cabecera.
    * Proteger un endpoint usando esta dependencia.
    * Explicar la diferencia entre Autenticación ("quién eres") y Autorización ("qué puedes hacer").
* **Temas a Dominar:**
    * Estructura de un JWT: Header, Payload, Signature.
    * OAuth2 y `OAuth2PasswordBearer` en FastAPI.
    * Hashing de contraseñas con `passlib` (nunca guardarlas en texto plano).
    * Creación (encode) y validación (decode) de tokens.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Almacena el JWT en una cookie `HttpOnly` en el navegador para protegerlo de ataques XSS.
    * **Error Común:** Poner información sensible en el payload del JWT. El payload es visible; solo está protegido contra manipulaciones, no contra lectura.
* **Mini-Proyecto:** Añade un modelo de `User` (con `username` y `hashed_password`). Implementa el endpoint `/token` y un endpoint protegido `/users/me` que devuelva los datos del usuario autenticado.

### OWASP Top 10 para APIs

* **Concepto Clave y Relevancia Profesional:** El OWASP Top 10 es una lista de referencia de los riesgos de seguridad más críticos. Conocerlos y saber mitigarlos es una señal de madurez profesional.
* **Objetivos de Aprendizaje Concretos:**
    * Explicar cómo el uso de un ORM previene la Inyección de SQL.
    * Describir cómo la validación de Pydantic mitiga problemas de Asignación Masiva.
    * Implementar limitación de tasa (rate limiting) para prevenir ataques de fuerza bruta.
* **Temas a Dominar:**
    * Inyección (SQL, etc.).
    * Autenticación Rota.
    * Autorización a Nivel de Objeto Rota (ej. poder ver `/users/123` cuando eres el usuario 456).
    * Uso de CORS en FastAPI.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Adopta un enfoque de "defensa en profundidad": combina validación de entrada, consultas parametrizadas, autorización a nivel de endpoint y de objeto.
    * **Error Común:** Configurar CORS con un comodín (`allow_origins=["*"]`) en producción. Sé explícito y lista solo los dominios de tu frontend.
* **Mini-Proyecto:** En tu API de tareas, asegura que un usuario solo pueda ver, actualizar o eliminar sus propias tareas, verificando que el `user_id` del token coincida con el `user_id` de la tarea.

### Gestión de Secretos

* **Concepto Clave y Relevancia Profesional:** Los secretos (claves de API, contraseñas de BD) nunca deben estar escritos en el código. Usar variables de entorno y cargarlas a través de Pydantic BaseSettings es la forma moderna y segura de gestionarlos.
* **Objetivos de Aprendizaje Concretos:**
    * Crear una clase de `Settings` que herede de Pydantic `BaseSettings` para cargar la configuración.
    * Crear un archivo `.env` para desarrollo local y asegurarse de que esté en `.gitignore`.
* **Temas a Dominar:**
    * Por qué nunca hacer "commit" de secretos a Git.
    * Variables de entorno y el archivo `.env`.
    * Uso de `pydantic_settings.BaseSettings`.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Crea un archivo `.env.example` en tu repositorio. Sirve como documentación de las variables de entorno necesarias.
    * **Error Común:** Cargar el archivo `.env` en producción. En producción, las variables se deben inyectar directamente en el entorno (ej. contenedor Docker), no a través de un archivo.
* **Mini-Proyecto:** Refactoriza tu API para que todas las configuraciones (URL de la BD, `JWT_SECRET_KEY`) se carguen desde variables de entorno a través de una clase `Settings`.

## Fase 7: Automatización y Despliegue con GitHub

*Escribir código es solo la mitad del trabajo. Entregarlo de forma fiable y automatizada es lo que te hace un ingeniero de ciclo completo.*

### Git y GitHub

* **Concepto Clave y Relevancia Profesional:** Git es el sistema de control de versiones estándar de la industria, y GitHub es la plataforma para alojar repositorios y colaborar. GitFlow (o una versión simplificada) es el flujo de trabajo para desarrollar funcionalidades de forma ordenada.
* **Objetivos de Aprendizaje Concretos:**
    * Crear una "feature branch" a partir de `develop`.
    * Hacer commits atómicos y descriptivos.
    * Abrir una "Pull Request" (PR) en GitHub.
* **Temas a Dominar:**
    * Ramas principales (`main`, `develop`) y de soporte (`feature/*`, `bugfix/*`).
    * El ciclo: `checkout`, `add`, `commit`, `push`, crear PR.
    * Revisión de código en Pull Requests.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Escribe buenos mensajes de commit. Sigue la convención "Conventional Commits" (ej. `feat: add user login endpoint`).
    * **Error Común:** Hacer "push" directamente a `main` o `develop`. Estas ramas deben estar protegidas, y todos los cambios deben pasar por una PR.
* **Mini-Proyecto:** Sube tu proyecto a un repositorio en GitHub. Practica el flujo creando una rama para una nueva funcionalidad, haciendo commits y abriendo una PR.

### Docker

* **Concepto Clave y Relevancia Profesional:** Docker "empaqueta" tu aplicación con todas sus dependencias en una unidad portable llamada "contenedor". Garantiza que la aplicación se ejecute exactamente igual en desarrollo, testing y producción.
* **Objetivos de Aprendizaje Concretos:**
    * Escribir un `Dockerfile` que construya una imagen para tu aplicación FastAPI.
    * Crear un archivo `docker-compose.yml` que orqueste la API, la base de datos PostgreSQL y el caché de Redis.
    * Levantar todo el entorno local con `docker-compose up`.
* **Temas a Dominar:**
    * Imágenes vs. Contenedores.
    * El `Dockerfile`: `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`.
    * `docker-compose.yml`: `services`, `image`, `build`, `ports`, `volumes`, `environment`.
    * Construcción de imágenes en múltiples etapas para reducir el tamaño final.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Usa imágenes base oficiales y específicas (ej. `python:3.11-slim`) y multi-stage builds para mantener la imagen de producción pequeña y segura.
    * **Error Común:** Incluir secretos o el directorio `.git` en la imagen. Usa un archivo `.dockerignore` para excluirlos.
* **Mini-Proyecto:** "Dockeriza" tu API de tareas. Crea el `Dockerfile` y el `docker-compose.yml` para levantar la API, PostgreSQL y Redis.

### CI/CD con GitHub Actions

* **Concepto Clave y Relevancia Profesional:** CI/CD (Integración Continua / Despliegue Continuo) es la práctica de automatizar las fases de construcción, prueba y despliegue. GitHub Actions permite definir flujos de trabajo que garantizan que cada cambio sea probado y desplegable.
* **Objetivos de Aprendizaje Concretos:**
    * Crear un workflow que se dispare en cada push a una PR.
    * Configurar un "job" que instale las dependencias con Poetry.
    * Añadir pasos para ejecutar linting (`ruff`) y pruebas automatizadas (`pytest`).
* **Temas a Dominar:**
    * Sintaxis de los archivos YAML de workflows.
    * Eventos, Jobs, steps y runners.
    * Uso de "actions" de la comunidad (ej. `actions/checkout@v3`).
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Haz que tus pipelines fallen rápido. Ejecuta los pasos más rápidos (linting) primero para ahorrar tiempo y recursos.
    * **Error Común:** No ejecutar las pruebas contra servicios reales (o dobles). Usa `services` en GitHub Actions para levantar una BD o Redis durante la ejecución de las pruebas.
* **Mini-Proyecto:** Crea un directorio `.github/workflows` y añade un archivo `ci.yml`. Configúralo para que en cada PR ejecute `poetry install`, un linter y tus pruebas de `pytest`.

## Fase 8: Ampliando el Stack: Django

*Entender un framework alternativo te da perspectiva y te hace un ingeniero más completo.*

### Concepto General y Componentes Clave

* **Concepto Clave y Relevancia Profesional:** Django es un framework "con baterías incluidas", ideal para aplicaciones web grandes y monolíticas. Conocerlo es valioso para trabajar en proyectos existentes o cuando se necesita un desarrollo rápido con un panel de administración robusto.
* **Objetivos de Aprendizaje Concretos:**
    * Describir la arquitectura Modelo-Vista-Template (MVT) de Django.
    * Generar una aplicación simple y explorar el panel de administración autogenerado.
    * Entender el rol de Django REST Framework (DRF) para construir APIs sobre Django.
* **Temas a Dominar:**
    * Filosofía "Baterías Incluidas" vs. "Micro" framework.
    * Arquitectura MVT (Modelo, Vista, Template).
    * El ORM de Django.
    * El Panel de Administración.
    * Django REST Framework (DRF).
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Si usas Django, aprovecha sus "baterías" (autenticación, ORM, admin). Intentar reemplazarlas es más complicado que usar un framework más ligero desde el principio.
    * **Error Común:** Forzar el asincronismo en partes de Django que no están diseñadas para ello. Aunque el soporte está mejorando, su núcleo sigue siendo predominantemente síncrono.
* **Mini-Proyecto:** Sigue el tutorial oficial de Django para crear la aplicación de encuestas. Enfócate en entender la filosofía, no en ser un experto.

## Fase 9: Introducción al Frontend: React

*Un desarrollador backend que entiende el frontend es 10 veces más efectivo.*

### Fundamentos de React y Hooks Esenciales

* **Concepto Clave y Relevancia Profesional:** React es una librería de JavaScript para construir interfaces de usuario a partir de componentes reutilizables. Los "Hooks" (`useState`, `useEffect`) permiten manejar el estado y el ciclo de vida en componentes funcionales.
* **Objetivos de Aprendizaje Concretos:**
    * Crear un componente funcional que reciba datos a través de `props`.
    * Utilizar el hook `useState` para manejar un estado simple.
    * Utilizar el hook `useEffect` para ejecutar una llamada a tu API de FastAPI cuando el componente se monta.
* **Temas a Dominar:**
    * JSX: La sintaxis que mezcla HTML y JavaScript.
    * Componentes Funcionales.
    * Props vs. State.
    * Hooks: `useState` y `useEffect`.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Descompón tu UI en componentes pequeños y reutilizables.
    * **Error Común:** Modificar el estado directamente. Siempre debes usar la función seteadora que te devuelve `useState` para que React sepa que debe volver a renderizar.
* **Mini-Proyecto:** Crea una aplicación de React simple que muestre una lista de tareas "hardcodeada".

### Comunicación con el Backend y Gestión de Estado

* **Concepto Clave y Relevancia Profesional:** Saber cómo conectar tu aplicación React a tu API de FastAPI usando herramientas como `fetch` o `axios` es el puente que une los dos mundos. La gestión de estado global permite compartir datos (como el usuario autenticado) a través de toda la aplicación.
* **Objetivos de Aprendizaje Concretos:**
    * Usar `fetch` o `axios` dentro de un `useEffect` para obtener la lista de tareas de tu API y guardarla en el estado.
    * Crear un formulario en React que, al enviarse, realice una petición POST a tu API para crear una nueva tarea.
* **Temas a Dominar:**
    * Llamadas a API con `fetch` o `axios`.
    * Manejo de promesas con `async/await`.
    * Gestión de estados de carga (loading) y error.
    * El Hook `useContext` para compartir estado.
* **Mejores Prácticas y Errores Comunes:**
    * **Mejor Práctica:** Centraliza tu lógica de llamadas a la API en funciones de servicio separadas (ej. `api.getTasks()`). Tus componentes no deberían construir las URLs.
    * **Error Común:** Olvidar el array de dependencias (`[]`) en `useEffect`. Sin él, una llamada a la API se ejecutará en un bucle infinito.
* **Mini-Proyecto:** Conecta tu frontend de React con tu backend de FastAPI. Implementa la funcionalidad completa: mostrar tareas, añadir tareas desde un formulario y eliminar tareas. (Bonus) Implementa un login que guarde el JWT.