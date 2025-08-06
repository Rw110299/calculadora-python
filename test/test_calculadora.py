import sys
import os

# Adiciona o diretório pai do arquivo atual ao sys.path para conseguir importar o módulo calculadora
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa as funções da calculadora para testar
from src.calculadora import somar, subtrair, multiplicar, dividir
import unittest

# Classe que agrupa os testes da calculadora, herdando da classe unittest.TestCase
class TestCalculadora(unittest.TestCase):

    # Testa se a função somar retorna a soma correta
    def test_somar(self):
        self.assertEqual(somar(1, 2), 3)

    # Testa se a função subtrair retorna a subtração correta
    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)

    # Testa se a função multiplicar retorna o produto correto
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 3), 9)

    # Testa se a função dividir retorna o quociente correto
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    # Testa se a divisão por zero levanta o erro correto (ZeroDivisionError)
    def test_divisao_por_zero(self):
        # Usa um contexto que espera que a função lançar uma exceção ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)

# Garante que os testes sejam executados quando rodar o arquivo diretamente
if __name__ == "__main__":
    unittest.main()
