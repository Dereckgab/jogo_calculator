from funcs import calculator, jogo

def menu():
    print("Escolha uma opção:")
    print("1. Calculadora")
    print("2. Jogo de Adivinhação")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        calculator.calculadora()
    elif escolha == '2':
        jogo.jogo_adivinhacao()
    else:
        print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    menu()
