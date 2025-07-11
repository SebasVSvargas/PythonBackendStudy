"""
PRUEBAS UNITARIAS - EJERCICIOS DE FUNDAMENTOS DE PYTHON
Estas pruebas validan que todas las funciones principales funcionan correctamente.
"""

import unittest
import sys
from pathlib import Path

# Agregar el directorio src al path para importar módulos
sys.path.append(str(Path(__file__).parent.parent / "src"))

try:
    from exercises.data_types import (
        salary_calculator, 
        validate_user_input, 
        text_processor,
        advanced_number_comparison,
        advanced_truthiness_checker
    )
    from exercises.control_flow import (
        authentication_system,
        enterprise_discount_calculator,
        status_checker_new_way,
        academic_grade_system
    )
    from exercises.loops import (
        process_company_data,
        generate_sales_report,
        advanced_dict_processor,
        modern_grade_processor
    )
except ImportError as e:
    print(f"Error importando módulos para testing: {e}")
    raise


class TestDataTypes(unittest.TestCase):
    """Pruebas para el módulo de tipos de datos."""
    
    def test_salary_calculator(self):
        """Prueba la calculadora de salarios."""
        result = salary_calculator(50000.0, 10, True, "test user")
        
        # Verificar que todos los campos requeridos están presentes
        self.assertIn('employee', result)
        self.assertIn('total_salary', result)
        self.assertIn('base_salary', result)
        self.assertIn('bonus', result)
        
        # Verificar que el nombre se formatea correctamente
        self.assertEqual(result['employee'], "Test User")
        
        # Verificar que tiene seguro
        self.assertTrue(result['has_insurance'])
    
    def test_validate_user_input(self):
        """Prueba el validador de datos de entrada."""
        # Datos válidos
        result = validate_user_input(25, "test@example.com", 85.0)
        self.assertTrue(result['is_valid'])
        self.assertEqual(result['level'], "Bueno")
        
        # Datos inválidos
        result = validate_user_input(15, "invalid-email", 150.0)
        self.assertFalse(result['is_valid'])
    
    def test_text_processor(self):
        """Prueba el procesador de texto."""
        text = "Python es genial"
        
        # Prueba análisis
        result = text_processor(text, "analyze")
        self.assertIn('word_count', result)
        self.assertEqual(result['word_count'], 3)
        
        # Prueba formateo
        result = text_processor(text, "format")
        self.assertIn('title_case', result)
        self.assertEqual(result['title_case'], "Python Es Genial")
    
    def test_advanced_number_comparison(self):
        """Prueba el comparador avanzado de números."""
        result = advanced_number_comparison(10, 5, 15)
        
        self.assertIn('statistics', result)
        self.assertEqual(result['statistics']['max'], 15)
        self.assertEqual(result['statistics']['min'], 5)
        self.assertEqual(result['relationship'], "num1 > num2")
    
    def test_advanced_truthiness_checker(self):
        """Prueba el verificador de veracidad."""
        # Valor truthy
        result = advanced_truthiness_checker("texto", "validation")
        self.assertTrue(result['is_truthy'])
        
        # Valor falsy
        result = advanced_truthiness_checker("", "validation")
        self.assertFalse(result['is_truthy'])


class TestControlFlow(unittest.TestCase):
    """Pruebas para el módulo de control de flujo."""
    
    def test_authentication_system(self):
        """Prueba el sistema de autenticación."""
        # Usuario válido
        result = authentication_system("admin", "admin123")
        self.assertTrue(result['success'])
        self.assertEqual(result['role'], "admin")
        self.assertIn('read', result['permissions'])
        self.assertIn('write', result['permissions'])
        
        # Usuario inválido
        result = authentication_system("admin", "wrong_password")
        self.assertFalse(result['success'])
        self.assertEqual(result['access_level'], "none")
    
    def test_enterprise_discount_calculator(self):
        """Prueba la calculadora de descuentos empresarial."""
        result = enterprise_discount_calculator(100.0, "vip", 10, "regular")
        
        self.assertIn('calculation_details', result)
        self.assertIn('customer_info', result)
        self.assertIn('final_price', result['calculation_details'])
        
        # VIP debería tener descuento
        details = result['calculation_details']
        original = float(details['subtotal'].replace('$', '').replace(',', ''))
        final = float(details['final_price'].replace('$', '').replace(',', ''))
        self.assertLess(final, original)
    
    def test_status_checker_new_way(self):
        """Prueba el verificador de códigos de estado."""
        # Código exitoso
        result = status_checker_new_way(200)
        self.assertEqual(result['message'], "OK")
        self.assertTrue(result['is_success'])
        self.assertFalse(result['is_client_error'])
        
        # Código de error del cliente
        result = status_checker_new_way(404)
        self.assertEqual(result['message'], "Not Found")
        self.assertFalse(result['is_success'])
        self.assertTrue(result['is_client_error'])
    
    def test_academic_grade_system(self):
        """Prueba el sistema de evaluación académica."""
        scores = [90, 85, 95, 88, 92]
        result = academic_grade_system(scores, "test student")
        
        self.assertIn('student_info', result)
        self.assertIn('scores_analysis', result)
        self.assertIn('grade_info', result)
        
        # Verificar cálculos
        expected_avg = sum(scores) / len(scores)
        self.assertEqual(result['scores_analysis']['average'], expected_avg)
        
        # Con este promedio debería estar aprobado
        self.assertTrue(result['grade_info']['passed'])


class TestLoops(unittest.TestCase):
    """Pruebas para el módulo de bucles."""
    
    def test_process_company_data(self):
        """Prueba el procesador de datos empresariales."""
        departments = [
            {
                "name": "IT",
                "budget": 100000,
                "employees": [
                    {"name": "Juan", "position": "Developer", "salary": 60000, "experience_years": 3}
                ]
            }
        ]
        
        result = process_company_data(departments)
        
        self.assertIn('company_summary', result)
        self.assertIn('department_details', result)
        self.assertEqual(result['company_summary']['total_departments'], 1)
        self.assertEqual(result['company_summary']['total_employees'], 1)
    
    def test_generate_sales_report(self):
        """Prueba el generador de reportes de ventas."""
        sales_data = [
            {"amount": 1000, "region": "Norte", "month": "Enero", "status": "completed"},
            {"amount": 1500, "region": "Sur", "month": "Enero", "status": "completed"}
        ]
        
        result = generate_sales_report(sales_data, 2000)
        
        self.assertIn('report_summary', result)
        self.assertEqual(result['report_summary']['successful_sales'], 2)
        self.assertEqual(result['report_summary']['achieved_revenue'], 2500)
        self.assertEqual(result['report_summary']['objective_status'], "Alcanzado")
    
    def test_advanced_dict_processor(self):
        """Prueba el procesador avanzado de diccionarios."""
        data = [
            {"name": "Ana", "age": 30, "salary": 50000},
            {"name": "Carlos", "age": 25, "salary": 45000}
        ]
        
        result = advanced_dict_processor(data, ["count", "aggregate"])
        
        self.assertIn('count_analysis', result)
        self.assertIn('aggregations', result)
        
        # Verificar conteo
        self.assertEqual(result['count_analysis']['total_items'], 2)
        
        # Verificar agregaciones
        if 'salary' in result['aggregations']:
            salary_agg = result['aggregations']['salary']
            self.assertEqual(salary_agg['average'], 47500)
            self.assertEqual(salary_agg['max'], 50000)
            self.assertEqual(salary_agg['min'], 45000)
    
    def test_modern_grade_processor(self):
        """Prueba el procesador moderno de calificaciones."""
        # Calificación excelente
        result = modern_grade_processor(95)
        self.assertEqual(result['letter_grade'], "A")
        self.assertEqual(result['gpa_points'], 4.0)
        self.assertTrue(result['passed'])
        
        # Calificación reprobatoria
        result = modern_grade_processor(45)
        self.assertEqual(result['letter_grade'], "F")
        self.assertEqual(result['gpa_points'], 0.0)
        self.assertFalse(result['passed'])


class TestIntegration(unittest.TestCase):
    """Pruebas de integración para verificar que los módulos funcionan juntos."""
    
    def test_all_modules_importable(self):
        """Verifica que todos los módulos se puedan importar sin errores."""
        # Si llegamos hasta aquí, las importaciones funcionaron
        self.assertTrue(True)
    
    def test_functions_return_expected_types(self):
        """Verifica que las funciones devuelven los tipos de datos esperados."""
        # Test data types functions
        result = salary_calculator(50000, 10, True, "test")
        self.assertIsInstance(result, dict)
        
        # Test control flow functions
        result = authentication_system("user", "pass")
        self.assertIsInstance(result, dict)
        
        # Test loops functions
        result = advanced_dict_processor([{"test": 1}], ["count"])
        self.assertIsInstance(result, dict)


def run_tests():
    """Ejecuta todas las pruebas y muestra un resumen."""
    print("🧪 EJECUTANDO PRUEBAS UNITARIAS")
    print("="*50)
    
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar todas las clases de prueba
    suite.addTests(loader.loadTestsFromTestCase(TestDataTypes))
    suite.addTests(loader.loadTestsFromTestCase(TestControlFlow))
    suite.addTests(loader.loadTestsFromTestCase(TestLoops))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Mostrar resumen
    print("\n" + "="*50)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"✅ Pruebas ejecutadas: {result.testsRun}")
    print(f"❌ Errores: {len(result.errors)}")
    print(f"⚠️  Fallas: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("🎉 ¡TODAS LAS PRUEBAS PASARON!")
    else:
        print("💔 Algunas pruebas fallaron.")
        
        if result.errors:
            print("\nErrores:")
            for test, error in result.errors:
                print(f"  - {test}: {error}")
        
        if result.failures:
            print("\nFallas:")
            for test, failure in result.failures:
                print(f"  - {test}: {failure}")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)