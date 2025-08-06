# Função que realiza a soma de dois números
def somar(a, b):
    return a + b  # Retorna a soma dos valores a e b

# Função que realiza a subtração de dois números
def subtrair(a, b):
    return a - b  # Retorna a diferença entre os valores a e b

# Função que realiza a multiplicação de dois números
def multiplicar(a, b):
    return a * b  # Retorna o produto dos valores a e b

# Função que realiza a divisão de dois números
def dividir(a, b):
    if b == 0:
        # Lança um erro se o valor de b for zero, pois não é possível dividir por zero
        raise ValueError("Divisão por zero não é permitida.")
    return a / b  # Retorna o resultado da divisão de a por b
