numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador da operação(+ , - ,* ou /): ")


if operador == "+":
    print(f"Resultado da adição: {numero1+numero2}")
elif operador == "-":
    print(f"Resultado da subtração: {numero1-numero2}")
elif operador == "/":
    print(f"Resultado da divisão: {numero1/numero2}")
elif operador == "*":
    print(f"Resultado da multiplicação: {numero1*numero2}")
else:
    print("operador inválido.")
    
    
    
