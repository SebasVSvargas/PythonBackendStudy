# 🐍 Ejercicios Prácticos: Fundamentos de Python Backend

## 🎯 Descripción del Proyecto

Este sistema de ejercicios está diseñado para enseñar los fundamentos de Python orientado al desarrollo backend, usando **casos prácticos del mundo real** en lugar de ejemplos triviales. Cada ejercicio simula problemas que encontrarás en tu carrera profesional como desarrollador backend.

### 🏆 Enfoque Profesional

- ✅ **Casos reales**: Sistemas de autenticación, cálculos financieros, procesamiento de inventarios
- ✅ **Mejores prácticas**: Uso de f-strings, refactorización con diccionarios, manejo de errores
- ✅ **Preparación profesional**: Te prepara para Django, FastAPI y microservicios
- ✅ **Código limpio**: Siguiendo estándares de la industria desde el primer día

## 📚 Módulos de Aprendizaje

### 1. 🧮 Sintaxis y Tipos de Datos
**Objetivos**: Dominar tipos primitivos, operadores y formateo profesional

**Ejercicios incluidos**:
- **💰 Calculadora de salarios empresarial**: Maneja diferentes tipos de datos, bonos, deducciones
- **✅ Validador de datos de entrada**: Simula validación de APIs con operadores lógicos
- **📝 Procesador de texto avanzado**: Análisis, formateo y validación de strings
- **📊 Comparador numérico con estadísticas**: Comparaciones complejas y análisis
- **🔍 Verificador de veracidad contextual**: Manejo de booleanos en diferentes contextos

### 2. 🔀 Control de Flujo
**Objetivos**: Implementar lógica de decisión profesional y refactorización

**Ejercicios incluidos**:
- **🎮 Juego 'Adivina el número' multinivel**: Control de flujo con múltiples dificultades
- **🔐 Sistema de autenticación y autorización**: Simula sistemas reales de login y permisos
- **💸 Calculadora de descuentos empresarial**: Lógica de negocio compleja con descuentos escalonados
- **🔄 Refactorización con diccionarios**: Comparación de métodos (if/elif vs diccionarios)
- **🎓 Sistema de evaluación académica**: Procesamiento de calificaciones con múltiples criterios

### 3. 🔄 Bucles e Iteración
**Objetivos**: Procesar datos complejos con bucles anidados y control de flujo

**Ejercicios incluidos**:
- **🏢 Procesador de datos empresariales**: Bucles anidados para análisis de departamentos
- **📊 Generador de reportes de ventas**: While loops con break/continue para objetivos
- **📦 Sistema de gestión de inventario**: Bucles complejos para procesar órdenes
- **🎯 Juego estadístico avanzado**: While con recolección de estadísticas
- **🔄 Procesador de listas de diccionarios**: Análisis avanzado de estructuras de datos

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.8 o superior
- Terminal/Línea de comandos

### Pasos de instalación

1. **Clonar o descargar el proyecto**
   ```bash
   # Si tienes git
   git clone <repository-url>
   
   # O descarga el ZIP y extrae los archivos
   ```

2. **Navegar al directorio del proyecto**
   ```bash
   cd python-fundamentals-exercises
   ```

3. **Instalar dependencias (opcional)**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el sistema principal**
   ```bash
   python src/main.py
   ```

### 🎮 Uso del Sistema

Al ejecutar `python src/main.py`, verás un menú interactivo:

```
📚 MÓDULOS DE PRÁCTICA DISPONIBLES:

1. 🧮 SINTAXIS Y TIPOS DE DATOS
2. 🔀 CONTROL DE FLUJO  
3. 🔄 BUCLES E ITERACIÓN
4. 📊 EJECUTAR TODOS LOS MÓDULOS
5. ℹ️  MOSTRAR INFORMACIÓN DEL PROYECTO
6. 🚪 SALIR
```

### 🔧 Ejecución de Módulos Individuales

También puedes ejecutar cada módulo por separado:

```bash
# Ejercicios de tipos de datos
python -c "from src.exercises.data_types import practice_data_types_system; practice_data_types_system()"

# Ejercicios de control de flujo
python -c "from src.exercises.control_flow import practice_control_flow_system; practice_control_flow_system()"

# Ejercicios de bucles
python -c "from src.exercises.loops import practice_loops_system; practice_loops_system()"
```

## 🏗️ Estructura del Proyecto

```
python-fundamentals-exercises/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias (actualmente vacío)
├── src/
│   ├── main.py              # Sistema principal interactivo
│   ├── exercises/
│   │   ├── __init__.py
│   │   ├── data_types.py    # Ejercicios de sintaxis y tipos
│   │   ├── control_flow.py  # Ejercicios de control de flujo
│   │   └── loops.py         # Ejercicios de bucles
│   └── utils/
│       ├── __init__.py
│       └── helpers.py       # Utilidades auxiliares
└── tests/
    ├── __init__.py
    └── test_exercises.py    # Pruebas unitarias
```

## 💡 Características Destacadas

### 🎯 Ejercicios del Mundo Real
- **Calculadora de salarios**: Simula sistemas de nómina empresarial
- **Sistema de autenticación**: Como los que usarías en Django/FastAPI
- **Gestión de inventario**: Procesamiento de datos como en e-commerce
- **Reportes de ventas**: Análisis de datos empresariales

### 🔧 Mejores Prácticas Integradas
- **Type hints**: Para mejor documentación del código
- **Docstrings**: Documentación profesional de funciones
- **F-strings**: Formateo moderno de cadenas
- **Manejo de errores**: Try/except apropiados
- **Refactorización**: Comparación de enfoques antiguos vs modernos

### 📊 Sistema Interactivo
- **Menús intuitivos**: Navegación fácil entre ejercicios
- **Demostraciones automáticas**: Para ver resultados rápidamente
- **Feedback inmediato**: Resultados visuales de cada ejercicio

## 🎓 Objetivos de Aprendizaje Específicos

Al completar estos ejercicios, serás capaz de:

### Sintaxis y Tipos de Datos
- [ ] Implementar funciones que manejen múltiples tipos de entrada
- [ ] Usar operadores lógicos y de comparación en casos complejos
- [ ] Aplicar f-strings para formateo profesional
- [ ] Validar datos de entrada como en APIs reales

### Control de Flujo
- [ ] Refactorizar bloques if/elif/else en versiones más eficientes
- [ ] Usar diccionarios para despacho en lugar de largas cadenas if/elif
- [ ] Implementar sistemas de autenticación básicos
- [ ] Manejar lógica de negocio compleja con múltiples criterios

### Bucles e Iteración
- [ ] Implementar al menos tres tipos de bucles (for, for anidado, while)
- [ ] Procesar listas de diccionarios con bucles complejos
- [ ] Usar break, continue y pass apropiadamente
- [ ] Optimizar bucles para casos de procesamiento de datos

## 🧪 Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
python -m pytest tests/

# Ejecutar pruebas con cobertura
python -m pytest tests/ --cov=src

# Ejecutar pruebas de un módulo específico
python -m pytest tests/test_exercises.py::TestDataTypes
```

## 🤝 Contribuir

Este proyecto está diseñado para aprendizaje. Si encuentras errores o tienes sugerencias:

1. Crea un issue describiendo el problema o mejora
2. Si quieres contribuir código, haz un fork y envía un pull request
3. Mantén el enfoque en casos prácticos y profesionales

## 📋 Roadmap de Mejoras

- [ ] Agregar más ejercicios de manipulación de archivos
- [ ] Incluir ejercicios con APIs REST básicas
- [ ] Agregar módulo de manejo de excepciones
- [ ] Crear ejercicios de testing unitario
- [ ] Integrar ejercicios con bases de datos SQLite

## 📖 Recursos Adicionales

### Para Profundizar:
- [Documentación oficial de Python](https://docs.python.org/3/)
- [Real Python](https://realpython.com/) - Tutoriales avanzados
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)

### Próximos Pasos en Backend:
- **Django**: Framework web completo
- **FastAPI**: Framework moderno para APIs
- **SQLAlchemy**: ORM para bases de datos
- **Pytest**: Testing avanzado

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**🚀 ¡Comienza tu viaje hacia convertirte en un desarrollador Python backend profesional!**