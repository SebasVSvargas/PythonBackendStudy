"""
EJERCICIOS PRÁCTICOS: SINTAXIS Y TIPOS DE DATOS
Fase 1 - Fundamentos de Python Backend

Objetivos de Aprendizaje:
1. Dominar los tipos de datos primitivos y sus operaciones
2. Implementar funciones que manejen diferentes tipos de entrada
3. Aplicar operadores lógicos y de comparación en casos reales
4. Usar f-strings para formateo profesional de cadenas
"""

def demonstrate_data_types():
    """Demostración básica de tipos de datos primitivos en Python"""
    # Integer
    integer_value = 10
    print(f"Integer: {integer_value} (Type: {type(integer_value).__name__})")

    # Float
    float_value = 10.5
    print(f"Float: {float_value} (Type: {type(float_value).__name__})")

    # String
    string_value = "Hello, Python!"
    print(f"String: {string_value} (Type: {type(string_value).__name__})")

    # Boolean
    boolean_value = True
    print(f"Boolean: {boolean_value} (Type: {type(boolean_value).__name__})")

    # None
    none_value = None
    print(f"None: {none_value} (Type: {type(none_value).__name__})")


# EJERCICIO 1: Calculadora de salarios con diferentes tipos de datos
def salary_calculator(base_salary: float, bonus_percentage: int, has_insurance: bool, employee_name: str) -> dict:
    """
    Calcula el salario total de un empleado considerando bonos y seguros.
    
    Args:
        base_salary: Salario base (float)
        bonus_percentage: Porcentaje de bono (int)
        has_insurance: Si tiene seguro médico (bool)
        employee_name: Nombre del empleado (str)
    
    Returns:
        dict: Información completa del salario
    """
    # Cálculo del bono
    bonus_amount = base_salary * (bonus_percentage / 100)
    
    # Deducción por seguro (si aplica)
    insurance_cost = 150.0 if has_insurance else 0.0
    
    # Salario total
    total_salary = base_salary + bonus_amount - insurance_cost
    
    # Uso de f-strings para formateo profesional
    return {
        'employee': employee_name.title(),
        'base_salary': f"${base_salary:,.2f}",
        'bonus': f"${bonus_amount:,.2f} ({bonus_percentage}%)",
        'insurance_deduction': f"${insurance_cost:,.2f}",
        'total_salary': f"${total_salary:,.2f}",
        'has_insurance': has_insurance
    }


# EJERCICIO 2: Validador de datos de entrada
def validate_user_input(age: int, email: str, score: float) -> dict:
    """
    Valida datos de entrada usando operadores lógicos y de comparación.
    
    Args:
        age: Edad del usuario
        email: Correo electrónico
        score: Puntuación (0.0 - 100.0)
    
    Returns:
        dict: Resultado de la validación
    """
    # Validaciones usando operadores de comparación y lógicos
    age_valid = 18 <= age <= 100
    email_valid = "@" in email and "." in email and len(email) >= 5
    score_valid = 0.0 <= score <= 100.0
    
    # Operador lógico AND para validación general
    is_valid = age_valid and email_valid and score_valid
    
    # Determinación del nivel basado en score
    if score >= 90.0:
        level = "Excelente"
    elif score >= 75.0:
        level = "Bueno"
    elif score >= 60.0:
        level = "Regular"
    else:
        level = "Necesita mejorar"
    
    return {
        'is_valid': is_valid,
        'age_valid': age_valid,
        'email_valid': email_valid,
        'score_valid': score_valid,
        'level': level,
        'summary': f"Usuario {'VÁLIDO' if is_valid else 'INVÁLIDO'} - Nivel: {level}"
    }


# EJERCICIO 3: Procesador de texto con operadores
def text_processor(text: str, operation: str = "analyze") -> dict:
    """
    Procesa texto usando diferentes operadores y métodos de string.
    
    Args:
        text: Texto a procesar
        operation: Tipo de operación ("analyze", "format", "validate")
    
    Returns:
        dict: Resultado del procesamiento
    """
    if not text or text is None:
        return {'error': 'Texto no válido'}
    
    # Análisis básico del texto
    word_count = len(text.split())
    char_count = len(text)
    char_count_no_spaces = len(text.replace(' ', ''))
    
    # Operaciones según el tipo solicitado
    if operation == "analyze":
        return {
            'original_text': text,
            'word_count': word_count,
            'character_count': char_count,
            'char_no_spaces': char_count_no_spaces,
            'is_long_text': word_count > 10,
            'contains_numbers': any(char.isdigit() for char in text),
            'is_uppercase': text.isupper(),
            'is_lowercase': text.islower()
        }
    
    elif operation == "format":
        return {
            'original': text,
            'title_case': text.title(),
            'upper_case': text.upper(),
            'lower_case': text.lower(),
            'reversed': text[::-1],
            'first_word': text.split()[0] if text.split() else '',
            'last_word': text.split()[-1] if text.split() else ''
        }
    
    elif operation == "validate":
        return {
            'text': text,
            'is_empty': len(text.strip()) == 0,
            'has_special_chars': not text.replace(' ', '').isalnum(),
            'min_length_met': len(text) >= 3,
            'max_length_met': len(text) <= 100,
            'valid_format': 3 <= len(text) <= 100 and len(text.strip()) > 0
        }
    
    else:
        return {'error': f'Operación "{operation}" no reconocida'}



# EJERCICIO 4: Comparador avanzado de números
def advanced_number_comparison(num1, num2, num3=None):
    """
    Función mejorada para comparar números con múltiples casos.
    
    Args:
        num1: Primer número
        num2: Segundo número  
        num3: Tercer número (opcional)
    
    Returns:
        dict: Resultado detallado de la comparación
    """
    # Validación de tipos
    if not all(isinstance(n, (int, float)) for n in [num1, num2] if n is not None):
        return {'error': 'Todos los valores deben ser números'}
    
    result = {
        'num1': num1,
        'num2': num2,
        'comparison_two': None,
        'statistics': {}
    }
    
    # Comparación básica entre num1 y num2
    if num1 > num2:
        result['comparison_two'] = f"{num1} es mayor que {num2}"
        result['relationship'] = "num1 > num2"
    elif num1 < num2:
        result['comparison_two'] = f"{num1} es menor que {num2}"
        result['relationship'] = "num1 < num2"
    else:
        result['comparison_two'] = f"{num1} es igual a {num2}"
        result['relationship'] = "num1 == num2"
    
    # Análisis de tres números si se proporciona num3
    if num3 is not None:
        if not isinstance(num3, (int, float)):
            result['error'] = 'num3 debe ser un número'
            return result
            
        numbers = [num1, num2, num3]
        result['num3'] = num3
        result['statistics'] = {
            'max': max(numbers),
            'min': min(numbers),
            'sum': sum(numbers),
            'average': sum(numbers) / len(numbers),
            'all_equal': num1 == num2 == num3,
            'ascending_order': numbers == sorted(numbers),
            'descending_order': numbers == sorted(numbers, reverse=True)
        }
    
    return result


# EJERCICIO 5: Verificador de veracidad avanzado
def advanced_truthiness_checker(value, context: str = "general"):
    """
    Verifica la veracidad de un valor en diferentes contextos.
    
    Args:
        value: Valor a verificar
        context: Contexto de verificación
    
    Returns:
        dict: Análisis detallado de veracidad
    """
    # Análisis básico de veracidad
    is_truthy = bool(value)
    value_type = type(value).__name__
    
    result = {
        'value': value,
        'type': value_type,
        'is_truthy': is_truthy,
        'context': context
    }
    
    # Análisis específico por tipo
    if isinstance(value, str):
        result['string_analysis'] = {
            'is_empty': len(value) == 0,
            'is_whitespace_only': value.isspace() if value else False,
            'length': len(value),
            'stripped_length': len(value.strip()) if value else 0
        }
    elif isinstance(value, (list, tuple, dict)):
        result['collection_analysis'] = {
            'is_empty': len(value) == 0,
            'length': len(value),
            'has_falsy_elements': any(not bool(item) for item in value) if isinstance(value, (list, tuple)) else None
        }
    elif isinstance(value, (int, float)):
        result['number_analysis'] = {
            'is_zero': value == 0,
            'is_positive': value > 0,
            'is_negative': value < 0
        }
    
    # Mensaje contextual
    if context == "validation":
        result['message'] = f"Valor {'VÁLIDO' if is_truthy else 'INVÁLIDO'} para validación"
    elif context == "authentication":
        result['message'] = f"Acceso {'PERMITIDO' if is_truthy else 'DENEGADO'}"
    elif context == "data_processing":
        result['message'] = f"Dato {'PROCESABLE' if is_truthy else 'OMITIDO'}"
    else:
        result['message'] = f"El valor {value} se considera {'verdadero' if is_truthy else 'falso'}"
    
    return result


# EJERCICIO 6: Sistema de práctica integrado
def practice_data_types_system():
    """
    Sistema integrado para practicar todos los conceptos de tipos de datos.
    """
    print("=== SISTEMA DE PRÁCTICA: SINTAXIS Y TIPOS DE DATOS ===\n")
    
    # Ejercicio 1: Calculadora de salarios
    print("1. CALCULADORA DE SALARIOS")
    print("-" * 30)
    employee_data = salary_calculator(5000.0, 15, True, "juan pérez")
    for key, value in employee_data.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()
    
    # Ejercicio 2: Validador de datos
    print("2. VALIDADOR DE DATOS")
    print("-" * 25)
    validation_result = validate_user_input(25, "test@email.com", 87.5)
    print(f"Resumen: {validation_result['summary']}")
    print(f"Detalles: Edad OK: {validation_result['age_valid']}, "
          f"Email OK: {validation_result['email_valid']}, "
          f"Score OK: {validation_result['score_valid']}")
    print()
    
    # Ejercicio 3: Procesador de texto
    print("3. PROCESADOR DE TEXTO")
    print("-" * 25)
    sample_text = "Python es un lenguaje poderoso para backend"
    analysis = text_processor(sample_text, "analyze")
    print(f"Texto: '{analysis['original_text']}'")
    print(f"Palabras: {analysis['word_count']}, Caracteres: {analysis['character_count']}")
    print(f"Contiene números: {analysis['contains_numbers']}")
    print()
    
    # Ejercicio 4: Comparador de números
    print("4. COMPARADOR DE NÚMEROS")
    print("-" * 30)
    comparison = advanced_number_comparison(15, 10, 20)
    print(f"Comparación: {comparison['comparison_two']}")
    if 'statistics' in comparison and comparison['statistics']:
        stats = comparison['statistics']
        print(f"Estadísticas: Max={stats['max']}, Min={stats['min']}, Promedio={stats['average']:.2f}")
    print()
    
    # Ejercicio 5: Verificador de veracidad
    print("5. VERIFICADOR DE VERACIDAD")
    print("-" * 35)
    test_values = [0, "", "texto", [], [1, 2, 3], None, True, False]
    for test_val in test_values:
        result = advanced_truthiness_checker(test_val, "validation")
        print(f"{str(test_val):10} ({result['type']:5}) -> {result['message']}")


# Ejemplo de uso y testing
if __name__ == "__main__":
    print("Ejecutando demostración básica...")
    demonstrate_data_types()
    print("\n" + "="*60 + "\n")
    
    print("Ejecutando sistema de práctica completo...")
    practice_data_types_system()