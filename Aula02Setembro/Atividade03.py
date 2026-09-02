import os
os.system("cls")

while True:
    try:
        numero = int(input("Digite um número inteiro:"))
        print(f"===TABUADA DE {numero}===")
        for i in range (10):
            print(f"{i+1} x {numero} = {numero*(i+1)}")
        break
    except:
        print("ERRO.ENTRADA INVÁLIDA. DIGITE APENAS NUMEROS!")
        