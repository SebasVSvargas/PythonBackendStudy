"""
EJERCICIOS PRÁCTICOS: BUCLES Y ITERACIÓN
Fase 1 - Fundamentos de Python Backend

Objetivos de Aprendizaje:
1. Implementar al menos tres tipos de bucles (for, for anidado, while)
2. Procesar listas de diccionarios con bucles complejos
3. Usar break, continue y pass apropiadamente
4. Optimizar bucles para casos del mundo real
"""

import random
import time
from typing import List, Dict, Any, Tuple


# EJERCICIO 1: Procesador de datos empresariales (Bucles anidados)
def process_company_data(departments: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Procesa datos de departamentos de una empresa usando bucles anidados.
    
    Args:
        departments: Lista de diccionarios con información de departamentos
    
    Returns:
        dict: Análisis completo de la empresa
    """
    if not departments:
        return {"error": "No hay datos de departamentos"}
    
    # Inicialización de contadores y acumuladores
    total_employees = 0
    total_budget = 0.0
    department_stats = {}
    employee_by_position = {}
    salary_ranges = {"high": 0, "medium": 0, "low": 0}
    
    print("🏢 Procesando datos empresariales...")
    print("=" * 50)
    
    # Bucle principal por departamentos
    for dept_index, department in enumerate(departments):
        dept_name = department.get("name", f"Departamento {dept_index + 1}")
        dept_budget = department.get("budget", 0)
        employees = department.get("employees", [])
        
        print(f"\n📊 Procesando: {dept_name}")
        
        # Inicializar estadísticas del departamento
        dept_employee_count = len(employees)
        dept_total_salary = 0
        dept_positions = {}
        
        # Bucle anidado por empleados del departamento
        for emp_index, employee in enumerate(employees):
            emp_name = employee.get("name", f"Empleado {emp_index + 1}")
            emp_position = employee.get("position", "Sin posición")
            emp_salary = employee.get("salary", 0)
            emp_experience = employee.get("experience_years", 0)
            
            # Procesar información del empleado
            print(f"   👤 {emp_name} - {emp_position} - ${emp_salary:,}")
            
            # Acumular totales
            total_employees += 1
            dept_total_salary += emp_salary
            
            # Contar posiciones
            if emp_position in dept_positions:
                dept_positions[emp_position] += 1
            else:
                dept_positions[emp_position] = 1
            
            # Contar posiciones globalmente
            if emp_position in employee_by_position:
                employee_by_position[emp_position] += 1
            else:
                employee_by_position[emp_position] = 1
            
            # Clasificar salarios
            if emp_salary >= 80000:
                salary_ranges["high"] += 1
            elif emp_salary >= 50000:
                salary_ranges["medium"] += 1
            else:
                salary_ranges["low"] += 1
        
        # Calcular estadísticas del departamento
        avg_salary = dept_total_salary / dept_employee_count if dept_employee_count > 0 else 0
        
        department_stats[dept_name] = {
            "employee_count": dept_employee_count,
            "total_salary_cost": dept_total_salary,
            "average_salary": avg_salary,
            "budget": dept_budget,
            "budget_utilization": (dept_total_salary / dept_budget * 100) if dept_budget > 0 else 0,
            "positions": dept_positions
        }
        
        total_budget += dept_budget
        
        print(f"   📈 Empleados: {dept_employee_count}")
        print(f"   💰 Costo salarial: ${dept_total_salary:,}")
        print(f"   📊 Salario promedio: ${avg_salary:,.2f}")
    
    return {
        "company_summary": {
            "total_departments": len(departments),
            "total_employees": total_employees,
            "total_budget": total_budget,
            "total_salary_cost": sum(dept["total_salary_cost"] for dept in department_stats.values()),
            "average_salary_company": sum(dept["total_salary_cost"] for dept in department_stats.values()) / total_employees if total_employees > 0 else 0
        },
        "department_details": department_stats,
        "position_distribution": employee_by_position,
        "salary_distribution": salary_ranges
    }


# EJERCICIO 2: Generador de reportes con while y control de flujo
def generate_sales_report(sales_data: List[Dict], target_revenue: float = 100000) -> Dict[str, Any]:
    """
    Genera reporte de ventas procesando datos hasta alcanzar objetivo.
    Usa while, break, continue para controlar el flujo.
    """
    if not sales_data:
        return {"error": "No hay datos de ventas"}
    
    # Variables de control
    current_revenue = 0.0
    processed_sales = 0
    successful_sales = 0
    failed_sales = 0
    sales_by_region = {}
    monthly_progress = {}
    
    # Usar while para procesar hasta alcanzar objetivo
    index = 0
    while index < len(sales_data) and current_revenue < target_revenue:
        sale = sales_data[index]
        
        # Validar datos de la venta
        sale_amount = sale.get("amount", 0)
        sale_region = sale.get("region", "Unknown")
        sale_month = sale.get("month", "Unknown")
        sale_status = sale.get("status", "pending")
        
        processed_sales += 1
        
        # Usar continue para saltar ventas canceladas
        if sale_status == "cancelled":
            print(f"⏭️  Venta #{processed_sales} cancelada - Saltando...")
            failed_sales += 1
            index += 1
            continue
        
        # Usar continue para saltar ventas con datos inválidos
        if sale_amount <= 0:
            print(f"❌ Venta #{processed_sales} con monto inválido - Saltando...")
            failed_sales += 1
            index += 1
            continue
        
        # Procesar venta válida
        current_revenue += sale_amount
        successful_sales += 1
        
        # Acumular por región
        if sale_region in sales_by_region:
            sales_by_region[sale_region] += sale_amount
        else:
            sales_by_region[sale_region] = sale_amount
        
        # Acumular por mes
        if sale_month in monthly_progress:
            monthly_progress[sale_month] += sale_amount
        else:
            monthly_progress[sale_month] = sale_amount
        
        print(f"✅ Venta #{processed_sales}: ${sale_amount:,} - Total: ${current_revenue:,}")
        
        # Verificar si alcanzamos el objetivo
        if current_revenue >= target_revenue:
            print(f"🎯 ¡Objetivo alcanzado! ${target_revenue:,}")
            break
        
        index += 1
    
    # Determinar status del objetivo
    if current_revenue >= target_revenue:
        objective_status = "Alcanzado"
        completion_percentage = 100.0
    else:
        objective_status = "No alcanzado"
        completion_percentage = (current_revenue / target_revenue) * 100
    
    return {
        "report_summary": {
            "target_revenue": target_revenue,
            "achieved_revenue": current_revenue,
            "completion_percentage": round(completion_percentage, 2),
            "objective_status": objective_status,
            "processed_sales": processed_sales,
            "successful_sales": successful_sales,
            "failed_sales": failed_sales
        },
        "regional_breakdown": sales_by_region,
        "monthly_progress": monthly_progress
    }


# EJERCICIO 3: Simulador de inventario con bucles complejos
def inventory_management_system(products: List[Dict], orders: List[Dict]) -> Dict[str, Any]:
    """
    Sistema de gestión de inventario con bucles complejos y lógica de negocio.
    """
    if not products or not orders:
        return {"error": "Faltan datos de productos u órdenes"}
    
    # Inicializar inventario
    inventory = {}
    for product in products:
        product_id = product.get("id")
        if product_id:
            inventory[product_id] = {
                "name": product.get("name", "Producto sin nombre"),
                "stock": product.get("initial_stock", 0),
                "price": product.get("price", 0.0),
                "reserved": 0,
                "sold": 0
            }
    
    processed_orders = []
    fulfilled_orders = 0
    rejected_orders = 0
    total_revenue = 0.0
    
    print("📦 Sistema de Gestión de Inventario")
    print("=" * 40)
    
    # Procesar órdenes con bucle for y lógica compleja
    for order_num, order in enumerate(orders, 1):
        order_id = order.get("id", f"ORDER_{order_num}")
        customer = order.get("customer", "Cliente desconocido")
        items = order.get("items", [])
        
        print(f"\n🛒 Procesando orden {order_id} - Cliente: {customer}")
        
        # Verificar disponibilidad de todos los items (bucle anidado)
        order_valid = True
        order_total = 0.0
        order_details = []
        
        for item in items:
            product_id = item.get("product_id")
            quantity = item.get("quantity", 0)
            
            if product_id not in inventory:
                print(f"   ❌ Producto {product_id} no encontrado")
                order_valid = False
                break
            
            product = inventory[product_id]
            available_stock = product["stock"] - product["reserved"]
            
            if quantity > available_stock:
                print(f"   ❌ Stock insuficiente para {product['name']} (Solicitado: {quantity}, Disponible: {available_stock})")
                order_valid = False
                break
            
            # Calcular precio del item
            item_total = quantity * product["price"]
            order_total += item_total
            
            order_details.append({
                "product_id": product_id,
                "product_name": product["name"],
                "quantity": quantity,
                "unit_price": product["price"],
                "total_price": item_total
            })
            
            print(f"   ✅ {product['name']} x{quantity} - ${item_total:,.2f}")
        
        # Procesar orden si es válida
        if order_valid and order_details:
            # Reservar inventario (segundo bucle para confirmación)
            for detail in order_details:
                product_id = detail["product_id"]
                quantity = detail["quantity"]
                inventory[product_id]["reserved"] += quantity
                inventory[product_id]["sold"] += quantity
            
            fulfilled_orders += 1
            total_revenue += order_total
            order_status = "Fulfilled"
            
            print(f"   💰 Total orden: ${order_total:,.2f}")
            print(f"   ✅ Orden completada exitosamente")
            
        else:
            rejected_orders += 1
            order_status = "Rejected"
            order_total = 0.0
            
            print(f"   ❌ Orden rechazada")
        
        processed_orders.append({
            "order_id": order_id,
            "customer": customer,
            "status": order_status,
            "total": order_total,
            "items": order_details
        })
    
    # Generar reporte final de inventario
    inventory_report = {}
    low_stock_products = []
    
    for product_id, product in inventory.items():
        current_stock = product["stock"] - product["sold"]
        inventory_report[product_id] = {
            "name": product["name"],
            "initial_stock": product["stock"],
            "sold": product["sold"],
            "current_stock": current_stock,
            "revenue_generated": product["sold"] * product["price"]
        }
        
        # Detectar productos con stock bajo
        if current_stock < 5:
            low_stock_products.append({
                "product_id": product_id,
                "name": product["name"],
                "current_stock": current_stock
            })
    
    return {
        "order_processing": {
            "total_orders": len(orders),
            "fulfilled_orders": fulfilled_orders,
            "rejected_orders": rejected_orders,
            "fulfillment_rate": (fulfilled_orders / len(orders)) * 100 if orders else 0,
            "total_revenue": total_revenue
        },
        "inventory_status": inventory_report,
        "alerts": {
            "low_stock_products": low_stock_products
        },
        "processed_orders": processed_orders
    }

# EJERCICIO 4: Juego "Adivina el número" avanzado con while
def guess_the_number_with_stats():
    """
    Versión avanzada del juego que registra estadísticas y patrones.
    """
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts_used = 0
    guess_history = []
    hint_count = 0
    
    print("🎯 ¡BIENVENIDO AL JUEGO 'ADIVINA EL NÚMERO' CON ESTADÍSTICAS! 🎯")
    print(f"📊 He elegido un número entre 1 y 100")
    print(f"🎯 Tienes {max_attempts} intentos para adivinarlo")
    print(f"💡 Puedes pedir pistas escribiendo 'pista'")
    
    # Bucle principal del juego usando while
    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        
        try:
            user_input = input(f"\n[Intento {attempts_used + 1}/{max_attempts}] Tu adivinanza (o 'pista'): ").strip().lower()
            
            # Manejo de pistas
            if user_input == "pista":
                hint_count += 1
                if hint_count <= 3:  # Máximo 3 pistas
                    if number_to_guess % 2 == 0:
                        print("💡 Pista: El número es par")
                    else:
                        print("💡 Pista: El número es impar")
                    
                    if hint_count >= 2:
                        if number_to_guess <= 25:
                            print("💡 Pista: El número está entre 1 y 25")
                        elif number_to_guess <= 50:
                            print("💡 Pista: El número está entre 26 y 50")
                        elif number_to_guess <= 75:
                            print("💡 Pista: El número está entre 51 y 75")
                        else:
                            print("💡 Pista: El número está entre 76 y 100")
                else:
                    print("❌ Ya usaste todas tus pistas")
                continue  # No contar como intento
            
            # Convertir a número
            guess = int(user_input)
            
            # Validar rango
            if guess < 1 or guess > 100:
                print("⚠️  El número debe estar entre 1 y 100")
                continue  # No contar como intento
            
            attempts_used += 1
            guess_history.append(guess)
            
            # Evaluar adivinanza
            if guess == number_to_guess:
                print(f"\n🎉 ¡FELICIDADES! 🎉")
                print(f"🏆 Has adivinado el número {number_to_guess} en {attempts_used} intentos")
                break
            else:
                difference = abs(guess - number_to_guess)
                
                # Pistas contextuales basadas en cercanía
                if difference == 1:
                    direction = "más alto" if guess < number_to_guess else "más bajo"
                    print(f"🔥 ¡MUY CERCA! Solo un poco {direction}")
                elif difference <= 5:
                    direction = "más alto" if guess < number_to_guess else "más bajo"
                    print(f"🌡️  ¡CALIENTE! Un poco {direction}")
                elif difference <= 10:
                    direction = "más alto" if guess < number_to_guess else "más bajo"
                    print(f"🌤️  Tibio... {direction}")
                else:
                    direction = "MÁS ALTO" if guess < number_to_guess else "MÁS BAJO"
                    print(f"🧊 Frío... {direction}")
                
                print(f"📊 Intentos restantes: {max_attempts - attempts_used}")
        
        except ValueError:
            print("❌ Por favor, ingresa un número válido o 'pista'")
            continue  # No contar como intento
    
    # Final del juego
    if attempts_used >= max_attempts:
        print(f"\n💔 Se acabaron los intentos. El número era {number_to_guess}")
    
    # Mostrar estadísticas
    print(f"\n📈 ESTADÍSTICAS DE LA PARTIDA:")
    print(f"🎯 Número objetivo: {number_to_guess}")
    print(f"🔢 Intentos usados: {attempts_used}/{max_attempts}")
    print(f"💡 Pistas usadas: {hint_count}")
    print(f"📊 Historial de intentos: {guess_history}")
    
    if guess_history:
        avg_guess = sum(guess_history) / len(guess_history)
        print(f"📊 Promedio de tus intentos: {avg_guess:.1f}")


# EJERCICIO 5: Procesador de listas de diccionarios avanzado
def advanced_dict_processor(data_list: List[Dict[str, Any]], operations: List[str] = None) -> Dict[str, Any]:
    """
    Procesador avanzado de listas de diccionarios con múltiples operaciones.
    
    Args:
        data_list: Lista de diccionarios a procesar
        operations: Lista de operaciones a realizar
    
    Returns:
        dict: Resultados del procesamiento
    """
    if not data_list:
        return {"error": "Lista de datos vacía"}
    
    if operations is None:
        operations = ["count", "aggregate", "filter", "transform"]
    
    results = {}
    
    print("🔄 Procesando lista de diccionarios...")
    
    # Operación: Conteo y análisis básico
    if "count" in operations:
        print("\n📊 Realizando conteo y análisis...")
        
        total_items = len(data_list)
        key_frequency = {}
        value_types = {}
        
        # Bucle para analizar estructura
        for index, item in enumerate(data_list):
            if not isinstance(item, dict):
                print(f"   ⚠️  Item {index + 1} no es un diccionario")
                continue
            
            # Analizar cada clave del diccionario
            for key, value in item.items():
                # Contar frecuencia de claves
                key_frequency[key] = key_frequency.get(key, 0) + 1
                
                # Analizar tipos de valores
                value_type = type(value).__name__
                if key not in value_types:
                    value_types[key] = {}
                value_types[key][value_type] = value_types[key].get(value_type, 0) + 1
        
        results["count_analysis"] = {
            "total_items": total_items,
            "key_frequency": key_frequency,
            "value_types": value_types
        }
    
    # Operación: Agregación de datos numéricos
    if "aggregate" in operations:
        print("\n📈 Realizando agregaciones numéricas...")
        
        numeric_aggregations = {}
        
        # Bucle para encontrar campos numéricos
        for item in data_list:
            if isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, (int, float)):
                        if key not in numeric_aggregations:
                            numeric_aggregations[key] = {
                                "values": [],
                                "sum": 0,
                                "count": 0,
                                "min": float('inf'),
                                "max": float('-inf')
                            }
                        
                        agg = numeric_aggregations[key]
                        agg["values"].append(value)
                        agg["sum"] += value
                        agg["count"] += 1
                        agg["min"] = min(agg["min"], value)
                        agg["max"] = max(agg["max"], value)
        
        # Calcular promedios y estadísticas finales
        for key, agg in numeric_aggregations.items():
            if agg["count"] > 0:
                agg["average"] = agg["sum"] / agg["count"]
                agg["range"] = agg["max"] - agg["min"]
                # No almacenar todos los valores en el resultado final
                del agg["values"]
        
        results["aggregations"] = numeric_aggregations
    
    # Operación: Filtrado de datos
    if "filter" in operations:
        print("\n🔍 Realizando filtrado de datos...")
        
        filtered_results = {
            "complete_records": [],
            "incomplete_records": [],
            "numeric_heavy": [],
            "text_heavy": []
        }
        
        for item in data_list:
            if isinstance(item, dict):
                # Verificar completitud
                has_empty_values = any(v is None or v == "" for v in item.values())
                
                if has_empty_values:
                    filtered_results["incomplete_records"].append(item)
                else:
                    filtered_results["complete_records"].append(item)
                
                # Clasificar por tipo de contenido
                numeric_count = sum(1 for v in item.values() if isinstance(v, (int, float)))
                text_count = sum(1 for v in item.values() if isinstance(v, str))
                
                if numeric_count > text_count:
                    filtered_results["numeric_heavy"].append(item)
                else:
                    filtered_results["text_heavy"].append(item)
        
        results["filtered_data"] = {
            "complete_records_count": len(filtered_results["complete_records"]),
            "incomplete_records_count": len(filtered_results["incomplete_records"]),
            "numeric_heavy_count": len(filtered_results["numeric_heavy"]),
            "text_heavy_count": len(filtered_results["text_heavy"])
        }
    
    return results


# EJERCICIO 6: Refactorización mejorada
def old_style_grade_processor(score: float) -> str:
    """Forma antigua de procesar calificaciones (NO recomendada)."""
    if score >= 90:
        return "A - Excelente"
    elif score >= 80:
        return "B - Muy Bueno"
    elif score >= 70:
        return "C - Bueno"
    elif score >= 60:
        return "D - Regular"
    else:
        return "F - Reprobado"


def modern_grade_processor(score: float) -> Dict[str, Any]:
    """Forma moderna usando diccionarios y rangos (RECOMENDADA)."""
    
    # Definir rangos de calificaciones
    grade_ranges = [
        (90, 100, {"letter": "A", "description": "Excelente", "gpa": 4.0, "status": "Honor Roll"}),
        (80, 89, {"letter": "B", "description": "Muy Bueno", "gpa": 3.0, "status": "Above Average"}),
        (70, 79, {"letter": "C", "description": "Bueno", "gpa": 2.0, "status": "Average"}),
        (60, 69, {"letter": "D", "description": "Regular", "gpa": 1.0, "status": "Below Average"}),
        (0, 59, {"letter": "F", "description": "Reprobado", "gpa": 0.0, "status": "Failing"})
    ]
    
    # Buscar el rango apropiado
    for min_score, max_score, grade_info in grade_ranges:
        if min_score <= score <= max_score:
            return {
                "score": score,
                "letter_grade": grade_info["letter"],
                "description": grade_info["description"],
                "gpa_points": grade_info["gpa"],
                "academic_status": grade_info["status"],
                "passed": score >= 60,
                "range": f"{min_score}-{max_score}"
            }
    
    # Caso de score fuera de rango
    return {
        "score": score,
        "error": "Score fuera de rango válido (0-100)",
        "letter_grade": "Invalid",
        "passed": False
    }


# EJERCICIO 7: Sistema de práctica integrado
def practice_loops_system():
    """
    Sistema integrado para practicar todos los conceptos de bucles.
    """
    print("🔄 === SISTEMA DE PRÁCTICA: BUCLES E ITERACIÓN === 🔄\n")
    
    while True:
        print("Selecciona un ejercicio:")
        print("1. 🏢 Procesador de Datos Empresariales (Bucles anidados)")
        print("2. 📊 Generador de Reportes de Ventas (While + control)")
        print("3. 📦 Sistema de Gestión de Inventario (Bucles complejos)")
        print("4. 🎯 Juego 'Adivina el Número' con Estadísticas")
        print("5. 🔄 Procesador Avanzado de Diccionarios")
        print("6. 📝 Demostración de Refactorización")
        print("7. 🚪 Salir")
        
        try:
            choice = int(input("\nTu elección (1-7): "))
            print("-" * 60)
            
            if choice == 1:
                # Demo de datos empresariales
                sample_departments = [
                    {
                        "name": "Desarrollo",
                        "budget": 500000,
                        "employees": [
                            {"name": "Ana García", "position": "Senior Developer", "salary": 85000, "experience_years": 5},
                            {"name": "Carlos López", "position": "Junior Developer", "salary": 45000, "experience_years": 2},
                            {"name": "María Rodríguez", "position": "Tech Lead", "salary": 95000, "experience_years": 8}
                        ]
                    },
                    {
                        "name": "Marketing",
                        "budget": 300000,
                        "employees": [
                            {"name": "Luis Martín", "position": "Marketing Manager", "salary": 70000, "experience_years": 6},
                            {"name": "Sofia Chen", "position": "Content Creator", "salary": 50000, "experience_years": 3}
                        ]
                    }
                ]
                
                result = process_company_data(sample_departments)
                print(f"\n📈 RESUMEN EJECUTIVO:")
                summary = result["company_summary"]
                print(f"Departamentos: {summary['total_departments']}")
                print(f"Empleados totales: {summary['total_employees']}")
                print(f"Presupuesto total: ${summary['total_budget']:,}")
                print(f"Costo salarial: ${summary['total_salary_cost']:,}")
                print(f"Salario promedio: ${summary['average_salary_company']:,.2f}")
                
            elif choice == 2:
                # Demo de reportes de ventas
                sample_sales = [
                    {"amount": 15000, "region": "Norte", "month": "Enero", "status": "completed"},
                    {"amount": 22000, "region": "Sur", "month": "Enero", "status": "completed"},
                    {"amount": 0, "region": "Este", "month": "Enero", "status": "cancelled"},
                    {"amount": 18000, "region": "Norte", "month": "Febrero", "status": "completed"},
                    {"amount": 25000, "region": "Oeste", "month": "Febrero", "status": "completed"},
                    {"amount": 30000, "region": "Sur", "month": "Marzo", "status": "completed"}
                ]
                
                result = generate_sales_report(sample_sales, 75000)
                summary = result["report_summary"]
                print(f"\n📊 REPORTE DE VENTAS:")
                print(f"Objetivo: ${summary['target_revenue']:,}")
                print(f"Logrado: ${summary['achieved_revenue']:,}")
                print(f"Progreso: {summary['completion_percentage']:.1f}%")
                print(f"Estado: {summary['objective_status']}")
                print(f"Ventas procesadas: {summary['successful_sales']}/{summary['processed_sales']}")
                
            elif choice == 3:
                # Demo de gestión de inventario
                sample_products = [
                    {"id": "PROD001", "name": "Laptop", "initial_stock": 50, "price": 1200.00},
                    {"id": "PROD002", "name": "Mouse", "initial_stock": 100, "price": 25.00},
                    {"id": "PROD003", "name": "Teclado", "initial_stock": 75, "price": 80.00}
                ]
                
                sample_orders = [
                    {
                        "id": "ORD001",
                        "customer": "Empresa ABC",
                        "items": [
                            {"product_id": "PROD001", "quantity": 5},
                            {"product_id": "PROD002", "quantity": 10}
                        ]
                    },
                    {
                        "id": "ORD002",
                        "customer": "Cliente XYZ",
                        "items": [
                            {"product_id": "PROD003", "quantity": 3}
                        ]
                    }
                ]
                
                result = inventory_management_system(sample_products, sample_orders)
                processing = result["order_processing"]
                print(f"\n📦 RESULTADO DE PROCESAMIENTO:")
                print(f"Órdenes totales: {processing['total_orders']}")
                print(f"Órdenes completadas: {processing['fulfilled_orders']}")
                print(f"Tasa de cumplimiento: {processing['fulfillment_rate']:.1f}%")
                print(f"Ingresos generados: ${processing['total_revenue']:,.2f}")
                
            elif choice == 4:
                guess_the_number_with_stats()
                
            elif choice == 5:
                # Demo de procesador de diccionarios
                sample_data = [
                    {"name": "Juan", "age": 30, "salary": 50000, "department": "IT"},
                    {"name": "María", "age": 25, "salary": 45000, "department": "Marketing"},
                    {"name": "Carlos", "age": 35, "salary": 60000, "department": "IT"},
                    {"name": "Ana", "age": 28, "salary": 55000, "department": "Sales"}
                ]
                
                result = advanced_dict_processor(sample_data, ["count", "aggregate"])
                print(f"\n🔄 ANÁLISIS DE DATOS:")
                if "count_analysis" in result:
                    count = result["count_analysis"]
                    print(f"Items procesados: {count['total_items']}")
                    print(f"Claves encontradas: {list(count['key_frequency'].keys())}")
                
                if "aggregations" in result:
                    agg = result["aggregations"]
                    for field, stats in agg.items():
                        print(f"{field}: Promedio = {stats['average']:.2f}, Rango = {stats['min']}-{stats['max']}")
                
            elif choice == 6:
                # Demostración de refactorización
                print("DEMO: Comparación de métodos")
                test_scores = [95, 85, 75, 65, 45]
                
                print("\n--- Método ANTIGUO ---")
                for score in test_scores:
                    result = old_style_grade_processor(score)
                    print(f"Score {score}: {result}")
                
                print("\n--- Método MODERNO ---")
                for score in test_scores:
                    result = modern_grade_processor(score)
                    print(f"Score {score}: {result['letter_grade']} - {result['description']} (GPA: {result['gpa_points']})")
                
            elif choice == 7:
                print("¡Gracias por practicar bucles! 🎉")
                break
                
            else:
                print("❌ Opción no válida. Elige entre 1-7.")
                
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
        
        print("\n" + "="*60 + "\n")


# Ejemplo de uso y testing
if __name__ == "__main__":
    print("🚀 Iniciando sistema de práctica de Bucles e Iteración...")
    practice_loops_system()