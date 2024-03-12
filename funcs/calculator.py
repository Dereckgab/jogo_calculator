import math

def calculadora():
    operacao = input ("escolha uma operação (+, -, *, /, R): ")

    if operacao == "R":
        num = float(input("informe seu numero "))
        resultado = round(math.sqrt(num), 1)
        print(f'o resultado da operação é: {resultado}')
    
    else:
        num_1 = int(input("Escolha uma numeração: "))
        num_2 = int(input("Escolha uma numeração: "))
        if operacao == "+":
            resultado = num_1 + num_2
            print("o resultado da operação é:", resultado)
        elif operacao == "-":
            resultado = num_1 - num_2
            print("o resultado da operação é:", resultado)
        elif operacao == "*":
            resultado = num_1 * num_2
            print("o resultado da operação é:", resultado)
        elif operacao == "/":
            resultado = num_1 / num_2
            print("o resultado da operação é:", resultado)
        else:
            print("Operação invalida")