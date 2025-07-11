"""
SISTEMA PRINCIPAL DE EJERCICIOS - FUNDAMENTOS DE PYTHON
Fase 1 - Python Backend Development

Este sistema integra todos los ejercicios prácticos para dominar:
- Sintaxis y tipos de datos
- Control de flujo  
- Bucles e iteración

Creado siguiendo las mejores prácticas profesionales.
"""

import sys
from pathlib import Path

# Agregar el directorio de ejercicios al path
sys.path.append(str(Path(__file__).parent / "exercises"))

try:
    from exercises.data_types import practice_data_types_system
    from exercises.control_flow import practice_control_flow_system  
    from exercises.loops import practice_loops_system
except ImportError as e:
    print(f"❌ Error importando módulos: {e}")
    print("Asegúrate de que todos los archivos de ejercicios estén en su lugar.")
    sys.exit(1)


def show_welcome_message():
    """Muestra el mensaje de bienvenida y objetivos."""
    print("🚀" + "="*70 + "🚀")
    print("    SISTEMA DE EJERCICIOS PRÁCTICOS - FUNDAMENTOS DE PYTHON")
    print("                     Fase 1: Backend Development")
    print("🚀" + "="*70 + "🚀")
    print()
    print("🎯 OBJETIVOS DE APRENDIZAJE:")
    print("   • Dominar sintaxis y tipos de datos primitivos")
    print("   • Implementar lógica de control de flujo profesional")  
    print("   • Usar bucles para procesar datos complejos")
    print("   • Aplicar mejores prácticas desde el primer día")
    print()
    print("💡 ENFOQUE PROFESIONAL:")
    print("   • Ejercicios basados en casos reales de backend")
    print("   • Técnicas usadas en equipos de desarrollo senior")
    print("   • Preparación para frameworks como Django/FastAPI")
    print()


def show_main_menu():
    """Muestra el menú principal del sistema."""
    print("📚 MÓDULOS DE PRÁCTICA DISPONIBLES:")
    print()
    print("1. 🧮 SINTAXIS Y TIPOS DE DATOS")
    print("   • Calculadora de salarios empresarial")
    print("   • Validador de datos de entrada")
    print("   • Procesador de texto avanzado")
    print("   • Comparador numérico con estadísticas")
    print("   • Verificador de veracidad contextual")
    print()
    print("2. 🔀 CONTROL DE FLUJO")
    print("   • Juego 'Adivina el número' multinivel")
    print("   • Sistema de autenticación y autorización")
    print("   • Calculadora de descuentos empresarial")
    print("   • Refactorización con diccionarios")
    print("   • Sistema de evaluación académica")
    print()
    print("3. 🔄 BUCLES E ITERACIÓN")
    print("   • Procesador de datos empresariales")
    print("   • Generador de reportes de ventas")
    print("   • Sistema de gestión de inventario")
    print("   • Juego estadístico avanzado")
    print("   • Procesador de listas de diccionarios")
    print()
    print("4. 📊 EJECUTAR TODOS LOS MÓDULOS")
    print("5. ℹ️  MOSTRAR INFORMACIÓN DEL PROYECTO")
    print("6. 🚪 SALIR")
    print()


def show_project_info():
    """Muestra información detallada del proyecto."""
    print("📋 INFORMACIÓN DEL PROYECTO")
    print("="*50)
    print()
    print("🎯 PROPÓSITO:")
    print("   Este sistema está diseñado para enseñar Python backend")
    print("   usando ejercicios prácticos del mundo real, no ejemplos")
    print("   triviales. Cada ejercicio simula problemas que encontrarás")
    print("   en tu carrera como desarrollador backend.")
    print()
    print("🏗️  ARQUITECTURA DEL PROYECTO:")
    print("   • src/exercises/data_types.py     - Tipos de datos")
    print("   • src/exercises/control_flow.py   - Control de flujo") 
    print("   • src/exercises/loops.py          - Bucles e iteración")
    print("   • src/main.py                     - Sistema principal")
    print("   • tests/                          - Pruebas unitarias")
    print()
    print("💼 APLICACIONES PROFESIONALES:")
    print("   • Validación de datos de APIs")
    print("   • Sistemas de autenticación")
    print("   • Procesamiento de inventarios")
    print("   • Cálculos financieros")
    print("   • Generación de reportes")
    print()
    print("📚 PREPARACIÓN PARA:")
    print("   • Django REST Framework")
    print("   • FastAPI")
    print("   • Desarrollo de microservicios")
    print("   • Sistemas de backend escalables")
    print()


def run_all_modules():
    """Ejecuta una demostración rápida de todos los módulos."""
    print("🚀 EJECUTANDO DEMOSTRACIÓN DE TODOS LOS MÓDULOS")
    print("="*60)
    
    print("\n1️⃣  MÓDULO: SINTAXIS Y TIPOS DE DATOS")
    print("-" * 45)
    try:
        from exercises.data_types import salary_calculator, validate_user_input
        
        # Demo rápida de calculadora de salarios
        result = salary_calculator(75000.0, 10, True, "demo user")
        print(f"✅ Demo Calculadora de Salarios:")
        print(f"   Empleado: {result['employee']}")
        print(f"   Salario total: {result['total_salary']}")
        
        # Demo rápida de validador
        validation = validate_user_input(25, "demo@example.com", 85.5)
        print(f"✅ Demo Validador de Datos:")
        print(f"   Resultado: {validation['summary']}")
        
    except Exception as e:
        print(f"❌ Error en módulo de tipos de datos: {e}")
    
    print("\n2️⃣  MÓDULO: CONTROL DE FLUJO")
    print("-" * 40)
    try:
        from exercises.control_flow import authentication_system, enterprise_discount_calculator
        
        # Demo rápida de autenticación
        auth_result = authentication_system("admin", "admin123")
        print(f"✅ Demo Sistema de Autenticación:")
        print(f"   Usuario: {auth_result.get('username', 'N/A')}")
        print(f"   Estado: {'Exitoso' if auth_result.get('success') else 'Fallido'}")
        
        # Demo rápida de descuentos
        discount_result = enterprise_discount_calculator(100.0, "vip", 15, "regular")
        print(f"✅ Demo Calculadora de Descuentos:")
        print(f"   Precio final: {discount_result['calculation_details']['final_price']}")
        print(f"   Descuento: {discount_result['calculation_details']['discount_percentage']}")
        
    except Exception as e:
        print(f"❌ Error en módulo de control de flujo: {e}")
    
    print("\n3️⃣  MÓDULO: BUCLES E ITERACIÓN")
    print("-" * 38)
    try:
        from exercises.loops import advanced_dict_processor
        
        # Demo rápida de procesador de diccionarios
        sample_data = [
            {"name": "Juan", "age": 30, "salary": 50000},
            {"name": "María", "age": 25, "salary": 45000}
        ]
        
        result = advanced_dict_processor(sample_data, ["count", "aggregate"])
        print(f"✅ Demo Procesador de Diccionarios:")
        if "count_analysis" in result:
            print(f"   Items procesados: {result['count_analysis']['total_items']}")
        if "aggregations" in result and "salary" in result["aggregations"]:
            avg_salary = result["aggregations"]["salary"]["average"]
            print(f"   Salario promedio: ${avg_salary:,.2f}")
        
    except Exception as e:
        print(f"❌ Error en módulo de bucles: {e}")
    
    print(f"\n🎉 DEMOSTRACIÓN COMPLETADA")
    print("💡 Para ejercicios interactivos completos, selecciona módulos individuales.")


def main():
    """Función principal del sistema."""
    show_welcome_message()
    
    while True:
        try:
            show_main_menu()
            choice = input("🎯 Selecciona una opción (1-6): ").strip()
            
            print("\n" + "="*80 + "\n")
            
            if choice == "1":
                print("🧮 INICIANDO MÓDULO: SINTAXIS Y TIPOS DE DATOS")
                print("-" * 55)
                practice_data_types_system()
                
            elif choice == "2":
                print("🔀 INICIANDO MÓDULO: CONTROL DE FLUJO")
                print("-" * 45)
                practice_control_flow_system()
                
            elif choice == "3":
                print("🔄 INICIANDO MÓDULO: BUCLES E ITERACIÓN")
                print("-" * 48)
                practice_loops_system()
                
            elif choice == "4":
                run_all_modules()
                
            elif choice == "5":
                show_project_info()
                
            elif choice == "6":
                print("👋 ¡Gracias por usar el sistema de ejercicios!")
                print("🎯 Continúa practicando para dominar Python backend.")
                print("🚀 ¡Éxito en tu carrera como desarrollador!")
                break
                
            else:
                print("❌ Opción no válida. Por favor, elige entre 1-6.")
            
            # Pausa antes de mostrar el menú nuevamente
            input("\n📱 Presiona Enter para continuar...")
            print("\n" + "🔄"*30 + " REGRESANDO AL MENÚ PRINCIPAL " + "🔄"*30 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido por el usuario.")
            print("¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            print("Por favor, reporta este error.")


if __name__ == "__main__":
    main()