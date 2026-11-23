# Calculadora de Operações (AV2 - 23\11\2026)


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")


def ler_numeros():
    """Pede dois números ao usuário e RETORNA os dois valores."""
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None 
    return a / b


def mostrar_resultado(operacao, resultado):
    """Recebe o nome da operação e o resultado como parâmetros."""
    if resultado is None:
        print("Erro: não é possível dividir por zero!")
    else:
        print(f"Resultado da {operacao}: {resultado:.2f}")



opcao = ""
while opcao != "5":
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando a calculadora. Até logo!")
    elif opcao in ["1", "2", "3", "4"]:
        n1, n2 = ler_numeros()

        if opcao == "1":
            mostrar_resultado("soma", somar(n1, n2))
        elif opcao == "2":
            mostrar_resultado("subtração", subtrair(n1, n2))
        elif opcao == "3":
            mostrar_resultado("multiplicação", multiplicar(n1, n2))
        else:
            mostrar_resultado("divisão", dividir(n1, n2))
    else:
        print("Opção inválida! Tente novamente.")