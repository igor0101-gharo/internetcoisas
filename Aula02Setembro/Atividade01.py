import os
os.system("cls")

print("====SOMA DE DOIS NÚMEROS====")
while True:
    try:
        numero1 = float(input("\nDigite o primeiro número: \n"))
        numero2 = float(input("\nDigite o segundo número:\n"))
        
        print(f"Resultado: {numero1+numero2}")
        break
    except:
        print("ERRO: DIGITE APENAS NÚMEROS.")