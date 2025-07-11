#!/usr/bin/env python3
"""
SCRIPT DE VERIFICACIÓN RÁPIDA
Verifica que todas las funciones principales estén funcionando correctamente.
"""

import sys
from pathlib import Path

# Agregar src al path
sys.path.append(str(Path(__file__).parent / "src"))

def test_imports():
    """Prueba que todos los módulos se puedan importar."""
    print("🔍 Verificando importaciones...")
    
    try:
        from exercises.data_types import salary_calculator
        print("✅ data_types.py - OK")
    except ImportError as e:
        print(f"❌ data_types.py - Error: {e}")
        return False
    
    try:
        from exercises.control_flow import authentication_system
        print("✅ control_flow.py - OK")
    except ImportError as e:
        print(f"❌ control_flow.py - Error: {e}")
        return False
    
    try:
        from exercises.loops import advanced_dict_processor
        print("✅ loops.py - OK")
    except ImportError as e:
        print(f"❌ loops.py - Error: {e}")
        return False
    
    return True

def test_basic_functionality():
    """Prueba funcionalidad básica de cada módulo."""
    print("\n🧪 Probando funcionalidad básica...")
    
    try:
        from exercises.data_types import salary_calculator
        result = salary_calculator(50000, 10, True, "test user")
        assert isinstance(result, dict)
        assert 'employee' in result
        print("✅ Calculadora de salarios - OK")
    except Exception as e:
        print(f"❌ Calculadora de salarios - Error: {e}")
        return False
    
    try:
        from exercises.control_flow import authentication_system
        result = authentication_system("admin", "admin123")
        assert isinstance(result, dict)
        assert 'success' in result
        print("✅ Sistema de autenticación - OK")
    except Exception as e:
        print(f"❌ Sistema de autenticación - Error: {e}")
        return False
    
    try:
        from exercises.loops import advanced_dict_processor
        result = advanced_dict_processor([{"test": 1}], ["count"])
        assert isinstance(result, dict)
        print("✅ Procesador de diccionarios - OK")
    except Exception as e:
        print(f"❌ Procesador de diccionarios - Error: {e}")
        return False
    
    return True

def main():
    """Función principal del script de verificación."""
    print("🚀 VERIFICACIÓN RÁPIDA DEL SISTEMA DE EJERCICIOS")
    print("="*60)
    
    # Verificar importaciones
    if not test_imports():
        print("\n❌ Fallo en las importaciones. Revisa los archivos de ejercicios.")
        return False
    
    # Verificar funcionalidad
    if not test_basic_functionality():
        print("\n❌ Fallo en la funcionalidad básica. Revisa la implementación.")
        return False
    
    print("\n🎉 ¡TODAS LAS VERIFICACIONES PASARON!")
    print("✅ El sistema está listo para usar")
    print("\n🎯 Para usar el sistema completo, ejecuta:")
    print("   python src/main.py")
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n💡 Puedes ejecutar el sistema principal ahora.")
    else:
        print("\n🔧 Por favor, revisa los errores antes de continuar.")
    
    sys.exit(0 if success else 1)
