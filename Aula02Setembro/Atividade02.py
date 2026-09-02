import os
os.system("cls")

while True:
    try:
        idade = int(input("\n\nDigite sua idade: "))
        
        if idade >= 18:
            print("Você é maior de idade.")
            break
        elif idade >= 0:
            print("Você é menor de idade.")
            break
        else:
            print("Digite uma idade válida.")
    except:
        print("ERRO. DIGITE UM VALOR VÁLIDO")