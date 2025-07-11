"""
EJERCICIOS PRÁCTICOS: CONTROL DE FLUJO
Fase 1 - Fundamentos de Python Backend

Objetivos de Aprendizaje:
1. Dominar estructuras de control if/elif/else
2. Implementar lógica de negocio con decisiones complejas
3. Refactorizar código usando diccionarios para despacho
4. Aplicar mejores prácticas en estructuras condicionales
"""

import random
from typing import Dict, List, Any


# EJERCICIO 1: Juego "Adivina el número" (Mejorado)
def guess_the_number_advanced():
    """
    Juego con múltiples niveles de dificultad.
    """
    print("🎯 ¡BIENVENIDO AL JUEGO 'ADIVINA EL NÚMERO' AVANZADO! 🎯")
    print("\nSelecciona tu nivel de dificultad:")
    print("1. Fácil (1-50, 15 intentos)")
    print("2. Medio (1-100, 10 intentos)")
    print("3. Difícil (1-200, 7 intentos)")
    print("4. Extremo (1-500, 5 intentos)")
    
    # Control de flujo para selección de dificultad
    while True:
        try:
            level = int(input("\nElige tu nivel (1-4): "))
            if level in [1, 2, 3, 4]:
                break
            else:
                print("❌ Por favor, elige un número entre 1 y 4.")
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
    
    # Configuración basada en nivel (usando diccionario)
    difficulty_config = {
        1: {"max_num": 50, "attempts": 15, "name": "Fácil"},
        2: {"max_num": 100, "attempts": 10, "name": "Medio"},
        3: {"max_num": 200, "attempts": 7, "name": "Difícil"},
        4: {"max_num": 500, "attempts": 5, "name": "Extremo"}
    }
    
    config = difficulty_config[level]
    number_to_guess = random.randint(1, config["max_num"])
    attempts_left = config["attempts"]
    
    print(f"\n🎮 Nivel: {config['name']}")
    print(f"📊 Rango: 1-{config['max_num']}")
    print(f"🎯 Intentos disponibles: {attempts_left}")
    print("¡Comencemos!")
    
    attempt_history = []
    
    for attempt in range(config["attempts"]):
        attempts_left = config["attempts"] - attempt
        print(f"\n--- Intento {attempt + 1} de {config['attempts']} ---")
        
        try:
            guess = int(input(f"Tu adivinanza (1-{config['max_num']}): "))
            
            # Validación del rango
            if guess < 1 or guess > config["max_num"]:
                print(f"⚠️  Número fuera de rango! Debe estar entre 1 y {config['max_num']}")
                continue
                
            attempt_history.append(guess)
            
            # Lógica principal del juego
            if guess < number_to_guess:
                difference = number_to_guess - guess
                if difference > 50:
                    print("📈 ¡MUCHO más alto!")
                elif difference > 20:
                    print("📈 Más alto")
                else:
                    print("📈 Un poco más alto")
                    
            elif guess > number_to_guess:
                difference = guess - number_to_guess
                if difference > 50:
                    print("📉 ¡MUCHO más bajo!")
                elif difference > 20:
                    print("📉 Más bajo")
                else:
                    print("📉 Un poco más bajo")
                    
            else:
                # ¡Victoria!
                print(f"\n🎉 ¡FELICIDADES! 🎉")
                print(f"🏆 Has adivinado el número {number_to_guess} en {attempt + 1} intentos!")
                print(f"📈 Historial de intentos: {attempt_history}")
                
                # Puntuación basada en intentos restantes
                score = (attempts_left - 1) * 10
                print(f"⭐ Puntuación: {score} puntos")
                return True
                
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
            continue
    
    # Si se acabaron los intentos
    print(f"\n💔 ¡Se acabaron los intentos!")
    print(f"🎯 El número era: {number_to_guess}")
    print(f"📈 Tu historial: {attempt_history}")
    return False


# EJERCICIO 2: Sistema de autenticación y autorización
def authentication_system(username: str, password: str, role: str = "user") -> Dict[str, Any]:
    """
    Sistema de autenticación con diferentes niveles de acceso.
    
    Args:
        username: Nombre de usuario
        password: Contraseña
        role: Rol del usuario (user, admin, moderator)
    
    Returns:
        dict: Resultado de la autenticación
    """
    # Base de datos simulada de usuarios
    users_db = {
        "admin": {"password": "admin123", "role": "admin"},
        "moderator": {"password": "mod123", "role": "moderator"},
        "user1": {"password": "user123", "role": "user"},
        "user2": {"password": "pass456", "role": "user"},
        "guest": {"password": "guest", "role": "guest"}
    }
    
    # Validaciones básicas
    if not username or not password:
        return {
            "success": False,
            "message": "Usuario y contraseña son requeridos",
            "access_level": "none"
        }
    
    # Verificación de existencia del usuario
    if username not in users_db:
        return {
            "success": False,
            "message": "Usuario no encontrado",
            "access_level": "none"
        }
    
    # Verificación de contraseña
    if users_db[username]["password"] != password:
        return {
            "success": False,
            "message": "Contraseña incorrecta",
            "access_level": "none"
        }
    
    # Usuario autenticado - determinar permisos
    user_role = users_db[username]["role"]
    
    # Sistema de permisos usando if/elif/else
    if user_role == "admin":
        permissions = ["read", "write", "delete", "manage_users", "system_config"]
        dashboard_url = "/admin-dashboard"
        message = "Bienvenido, Administrador. Acceso completo al sistema."
    elif user_role == "moderator":
        permissions = ["read", "write", "moderate_content", "manage_comments"]
        dashboard_url = "/moderator-dashboard"
        message = "Bienvenido, Moderador. Acceso a funciones de moderación."
    elif user_role == "user":
        permissions = ["read", "write_own", "comment"]
        dashboard_url = "/user-dashboard"
        message = "Bienvenido, Usuario. Acceso estándar al sistema."
    else:  # guest
        permissions = ["read"]
        dashboard_url = "/guest-dashboard"
        message = "Bienvenido, Invitado. Acceso de solo lectura."
    
    return {
        "success": True,
        "message": message,
        "username": username,
        "role": user_role,
        "permissions": permissions,
        "dashboard_url": dashboard_url,
        "access_level": "full" if user_role in ["admin", "moderator"] else "limited"
    }


# EJERCICIO 3: Calculadora de descuentos empresarial
def enterprise_discount_calculator(price: float, customer_type: str, quantity: int, season: str = "regular") -> Dict[str, Any]:
    """
    Calcula descuentos basados en múltiples criterios empresariales.
    
    Args:
        price: Precio base del producto
        customer_type: Tipo de cliente (vip, premium, regular, new)
        quantity: Cantidad de productos
        season: Temporada (regular, black_friday, christmas, summer_sale)
    
    Returns:
        dict: Detalles del cálculo de descuento
    """
    if price <= 0 or quantity <= 0:
        return {"error": "Precio y cantidad deben ser mayores a 0"}
    
    # Descuentos base por tipo de cliente
    if customer_type == "vip":
        base_discount = 0.20  # 20%
        customer_tier = "VIP"
    elif customer_type == "premium":
        base_discount = 0.15  # 15%
        customer_tier = "Premium"
    elif customer_type == "regular":
        base_discount = 0.05  # 5%
        customer_tier = "Regular"
    elif customer_type == "new":
        base_discount = 0.10  # 10% (descuento especial para nuevos)
        customer_tier = "Nuevo Cliente"
    else:
        base_discount = 0.0
        customer_tier = "Sin clasificar"
    
    # Descuentos por cantidad (escalonados)
    if quantity >= 100:
        quantity_discount = 0.15  # 15%
        quantity_tier = "Mayorista"
    elif quantity >= 50:
        quantity_discount = 0.10  # 10%
        quantity_tier = "Medio Mayorista"
    elif quantity >= 20:
        quantity_discount = 0.07  # 7%
        quantity_tier = "Volumen Alto"
    elif quantity >= 10:
        quantity_discount = 0.05  # 5%
        quantity_tier = "Volumen Medio"
    else:
        quantity_discount = 0.0
        quantity_tier = "Volumen Bajo"
    
    # Descuentos estacionales
    seasonal_discounts = {
        "black_friday": 0.25,    # 25%
        "christmas": 0.20,       # 20%
        "summer_sale": 0.15,     # 15%
        "regular": 0.0           # 0%
    }
    
    seasonal_discount = seasonal_discounts.get(season, 0.0)
    
    # Cálculo del descuento total (no acumulativo directo, aplicado en cascada)
    subtotal = price * quantity
    
    # Aplicar descuento de cliente
    after_customer_discount = subtotal * (1 - base_discount)
    customer_savings = subtotal - after_customer_discount
    
    # Aplicar descuento por cantidad sobre el subtotal ya descontado
    after_quantity_discount = after_customer_discount * (1 - quantity_discount)
    quantity_savings = after_customer_discount - after_quantity_discount
    
    # Aplicar descuento estacional sobre el resultado anterior
    final_price = after_quantity_discount * (1 - seasonal_discount)
    seasonal_savings = after_quantity_discount - final_price
    
    total_savings = subtotal - final_price
    total_discount_percentage = (total_savings / subtotal) * 100
    
    return {
        "calculation_details": {
            "original_price": f"${price:.2f}",
            "quantity": quantity,
            "subtotal": f"${subtotal:.2f}",
            "final_price": f"${final_price:.2f}",
            "total_savings": f"${total_savings:.2f}",
            "discount_percentage": f"{total_discount_percentage:.1f}%"
        },
        "customer_info": {
            "type": customer_type,
            "tier": customer_tier,
            "discount": f"{base_discount*100:.0f}%",
            "savings": f"${customer_savings:.2f}"
        },
        "quantity_info": {
            "quantity": quantity,
            "tier": quantity_tier,
            "discount": f"{quantity_discount*100:.0f}%",
            "savings": f"${quantity_savings:.2f}"
        },
        "seasonal_info": {
            "season": season,
            "discount": f"{seasonal_discount*100:.0f}%",
            "savings": f"${seasonal_savings:.2f}"
        },
        "recommendation": get_purchase_recommendation(total_discount_percentage)
    }


def get_purchase_recommendation(discount_percentage: float) -> str:
    """Genera recomendación basada en el descuento total."""
    if discount_percentage >= 40:
        return "🔥 ¡EXCELENTE OFERTA! Es el momento perfecto para comprar."
    elif discount_percentage >= 25:
        return "👍 Muy buena oferta. Recomendamos aprovechar."
    elif discount_percentage >= 15:
        return "✅ Oferta decente. Considera comprar si necesitas el producto."
    elif discount_percentage >= 5:
        return "📊 Descuento básico aplicado."
    else:
        return "💡 Sin descuentos especiales. Precio regular."


# EJERCICIO 4: Refactorización usando diccionarios (Mejor práctica)
def status_checker_old_way(status_code: int) -> str:
    """
    Forma ANTIGUA de manejar códigos de estado (NO recomendada).
    Esta es la forma que debes EVITAR.
    """
    if status_code == 200:
        return "OK - Solicitud exitosa"
    elif status_code == 201:
        return "Created - Recurso creado"
    elif status_code == 400:
        return "Bad Request - Solicitud incorrecta"
    elif status_code == 401:
        return "Unauthorized - No autorizado"
    elif status_code == 403:
        return "Forbidden - Prohibido"
    elif status_code == 404:
        return "Not Found - No encontrado"
    elif status_code == 500:
        return "Internal Server Error - Error del servidor"
    elif status_code == 502:
        return "Bad Gateway - Gateway incorrecto"
    elif status_code == 503:
        return "Service Unavailable - Servicio no disponible"
    else:
        return "Unknown Status - Estado desconocido"


def status_checker_new_way(status_code: int) -> Dict[str, Any]:
    """
    Forma MODERNA y EFICIENTE usando diccionarios (RECOMENDADA).
    Esta es la forma profesional de hacerlo.
    """
    # Diccionario de despacho - mucho más limpio y eficiente
    status_codes = {
        200: {"message": "OK", "description": "Solicitud exitosa", "category": "success"},
        201: {"message": "Created", "description": "Recurso creado", "category": "success"},
        400: {"message": "Bad Request", "description": "Solicitud incorrecta", "category": "client_error"},
        401: {"message": "Unauthorized", "description": "No autorizado", "category": "client_error"},
        403: {"message": "Forbidden", "description": "Prohibido", "category": "client_error"},
        404: {"message": "Not Found", "description": "No encontrado", "category": "client_error"},
        500: {"message": "Internal Server Error", "description": "Error del servidor", "category": "server_error"},
        502: {"message": "Bad Gateway", "description": "Gateway incorrecto", "category": "server_error"},
        503: {"message": "Service Unavailable", "description": "Servicio no disponible", "category": "server_error"}
    }
    
    # Obtener información del código o usar valores por defecto
    status_info = status_codes.get(status_code, {
        "message": "Unknown Status",
        "description": "Estado desconocido",
        "category": "unknown"
    })
    
    # Añadir información adicional
    status_info["code"] = status_code
    status_info["is_success"] = status_code < 400
    status_info["is_client_error"] = 400 <= status_code < 500
    status_info["is_server_error"] = status_code >= 500
    
    return status_info


# EJERCICIO 5: Sistema de evaluación académica
def academic_grade_system(scores: List[float], student_name: str) -> Dict[str, Any]:
    """
    Sistema complejo de evaluación académica con múltiples criterios.
    
    Args:
        scores: Lista de calificaciones (0-100)
        student_name: Nombre del estudiante
    
    Returns:
        dict: Evaluación completa del estudiante
    """
    if not scores or not all(0 <= score <= 100 for score in scores):
        return {"error": "Todas las calificaciones deben estar entre 0 y 100"}
    
    # Cálculos básicos
    average = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    # Determinación de la letra de calificación usando if/elif/else
    if average >= 95:
        letter_grade = "A+"
        performance = "Excelente"
        status = "Aprobado con Distinción"
    elif average >= 90:
        letter_grade = "A"
        performance = "Sobresaliente"
        status = "Aprobado con Mérito"
    elif average >= 85:
        letter_grade = "B+"
        performance = "Muy Bueno"
        status = "Aprobado"
    elif average >= 80:
        letter_grade = "B"
        performance = "Bueno"
        status = "Aprobado"
    elif average >= 75:
        letter_grade = "C+"
        performance = "Satisfactorio"
        status = "Aprobado"
    elif average >= 70:
        letter_grade = "C"
        performance = "Suficiente"
        status = "Aprobado"
    elif average >= 60:
        letter_grade = "D"
        performance = "Deficiente"
        status = "Reprobado"
    else:
        letter_grade = "F"
        performance = "Insuficiente"
        status = "Reprobado"
    
    # Análisis de consistencia
    score_range = max_score - min_score
    if score_range <= 5:
        consistency = "Muy Consistente"
    elif score_range <= 15:
        consistency = "Consistente"
    elif score_range <= 25:
        consistency = "Moderadamente Consistente"
    else:
        consistency = "Inconsistente"
    
    # Recomendaciones
    if average >= 90:
        recommendation = "Continúa con el excelente trabajo. Considera cursos avanzados."
    elif average >= 80:
        recommendation = "Buen rendimiento. Mantén el esfuerzo constante."
    elif average >= 70:
        recommendation = "Rendimiento aceptable. Busca apoyo en áreas débiles."
    else:
        recommendation = "Necesitas mejorar significativamente. Considera tutoría adicional."
    
    return {
        "student_info": {
            "name": student_name.title(),
            "total_assignments": len(scores),
            "status": status
        },
        "scores_analysis": {
            "individual_scores": scores,
            "average": round(average, 2),
            "max_score": max_score,
            "min_score": min_score,
            "range": score_range,
            "consistency": consistency
        },
        "grade_info": {
            "letter_grade": letter_grade,
            "performance_level": performance,
            "passed": average >= 70
        },
        "recommendation": recommendation
    }


# EJERCICIO 6: Sistema integrado de práctica
def practice_control_flow_system():
    """
    Sistema integrado para practicar todos los conceptos de control de flujo.
    """
    print("🎯 === SISTEMA DE PRÁCTICA: CONTROL DE FLUJO === 🎯\n")
    
    while True:
        print("Selecciona un ejercicio:")
        print("1. 🎮 Juego 'Adivina el Número' Avanzado")
        print("2. 🔐 Sistema de Autenticación")
        print("3. 💰 Calculadora de Descuentos Empresarial")
        print("4. 📊 Comparación de Métodos (if/elif vs diccionarios)")
        print("5. 🎓 Sistema de Evaluación Académica")
        print("6. 🏃 Salir")
        
        try:
            choice = int(input("\nTu elección (1-6): "))
            print("-" * 50)
            
            if choice == 1:
                guess_the_number_advanced()
                
            elif choice == 2:
                print("DEMO: Sistema de Autenticación")
                test_users = [
                    ("admin", "admin123"),
                    ("user1", "user123"),
                    ("guest", "guest"),
                    ("invalid", "wrong")
                ]
                
                for username, password in test_users:
                    result = authentication_system(username, password)
                    print(f"\nUsuario: {username}")
                    print(f"Resultado: {result['message']}")
                    if result['success']:
                        print(f"Permisos: {', '.join(result['permissions'])}")
                        
            elif choice == 3:
                print("DEMO: Calculadora de Descuentos")
                # Ejemplo de cálculo
                result = enterprise_discount_calculator(100.0, "vip", 25, "black_friday")
                print(f"\nProducto: $100.00 x 25 unidades")
                print(f"Cliente VIP en Black Friday")
                print(f"Precio final: {result['calculation_details']['final_price']}")
                print(f"Ahorro total: {result['calculation_details']['total_savings']}")
                print(f"Descuento: {result['calculation_details']['discount_percentage']}")
                print(f"Recomendación: {result['recommendation']}")
                
            elif choice == 4:
                print("DEMO: Comparación de Métodos")
                test_codes = [200, 404, 500, 999]
                
                print("\n--- Método ANTIGUO (if/elif/else) ---")
                for code in test_codes:
                    result = status_checker_old_way(code)
                    print(f"Código {code}: {result}")
                
                print("\n--- Método MODERNO (diccionarios) ---")
                for code in test_codes:
                    result = status_checker_new_way(code)
                    print(f"Código {code}: {result['message']} - {result['description']}")
                    
            elif choice == 5:
                print("DEMO: Sistema de Evaluación Académica")
                sample_scores = [88, 92, 85, 90, 87]
                result = academic_grade_system(sample_scores, "Ana García")
                
                print(f"\nEstudiante: {result['student_info']['name']}")
                print(f"Calificaciones: {result['scores_analysis']['individual_scores']}")
                print(f"Promedio: {result['scores_analysis']['average']}")
                print(f"Calificación: {result['grade_info']['letter_grade']} ({result['grade_info']['performance_level']})")
                print(f"Estado: {result['student_info']['status']}")
                print(f"Recomendación: {result['recommendation']}")
                
            elif choice == 6:
                print("¡Gracias por practicar! 🎉")
                break
                
            else:
                print("❌ Opción no válida. Elige entre 1-6.")
                
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
        
        print("\n" + "="*50 + "\n")


# Ejemplo de uso y testing
if __name__ == "__main__":
    print("🚀 Iniciando sistema de práctica de Control de Flujo...")
    practice_control_flow_system()