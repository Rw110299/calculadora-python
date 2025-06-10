from calculadora import somar, subtrair, multiplicar, dividir

def menu():
    print("Calculadora Simples em Python")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    escolha = input("Escolha uma operação (1-4): ")

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == "1":
        print("Resultado:", somar(a, b))
    elif escolha == "2":
        print("Resultado:", subtrair(a, b))
    elif escolha == "3":
        print("Resultado:", multiplicar(a, b))
    elif escolha == "4":
        try:
            print("Resultado:", dividir(a, b))
        except ValueError as e:
            print("Erro:", e)
    else:
        print("Opção inválida.")
if __name__ == "__main__":
    menu()