# Importa as funções de cálculo definidas no módulo calculadora.py
from calculadora import somar, subtrair, multiplicar, dividir

# Função que exibe o menu e executa a operação escolhida pelo usuário
def menu():
    print("Calculadora Simples em Python")  # Título da calculadora
    print("1. Somar")                       # Opção 1: Soma
    print("2. Subtrair")                    # Opção 2: Subtração
    print("3. Multiplicar")                 # Opção 3: Multiplicação
    print("4. Dividir")                     # Opção 4: Divisão

    # Solicita ao usuário que escolha uma das operações
    escolha = input("Escolha uma operação (1-4): ")

    # Solicita os dois números que serão utilizados na operação
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    # Executa a operação correspondente à escolha do usuário
    if escolha == "1":
        print("Resultado:", somar(a, b))  # Chama a função de soma
    elif escolha == "2":
        print("Resultado:", subtrair(a, b))  # Chama a função de subtração
    elif escolha == "3":
        print("Resultado:", multiplicar(a, b))  # Chama a função de multiplicação
    elif escolha == "4":
        try:
            # Tenta realizar a divisão, tratando erro de divisão por zero
            print("Resultado:", dividir(a, b))
        except ValueError as e:
            # Exibe a mensagem de erro se a divisão não for possível
            print("Erro:", e)
    else:
        # Caso o usuário digite uma opção inválida
        print("Opção inválida.")

# Este bloco garante que o menu só será executado se o arquivo for executado diretamente
if __name__ == "__main__":
    menu()
