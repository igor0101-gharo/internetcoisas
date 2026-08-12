numeroA = int(input("Digite o primeiro número: "))
numeroB = int(input("Digite o segundo número: "))

if numeroA > numeroB:
    print(f"{numeroA} é maior que {numeroB}")
elif numeroB > numeroA:
    print(f"{numeroB} é maior que {numeroA}")
elif numeroA == numeroB:
    print("os números são iguais")