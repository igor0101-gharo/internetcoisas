

while True:
    senha = input("Digite uma senha de quatros digitos: \n")
    quant = len(senha)
    
    if quant == 4:
        if senha.isdigit():
            print("Senha cadastrada com sucesso.")
            break
        else:
            print("Senha inválida.(digite apenas números)")
    else:
       print("Senha inválida.(mais que 4 digitos)")