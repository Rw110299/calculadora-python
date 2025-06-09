import unittest
from src.calculadora import somar, subtrair, multiplicar, dividir
class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(1, 2), 3)
    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 3), 9)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)

if __name__ == "__main__":
    unittest.main()