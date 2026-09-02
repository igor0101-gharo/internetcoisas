import os
os.system("cls")

while True:
    try:
        saldo =float(input("Digite o seu saldo:\n"))
        saque =float(input("Digite o quanto quer sacar:\n"))
        
        if saldo >= saque and saque >= 0:
            saldo_restante = saldo - saque
            print("Saque realizado com sucesso!")
            print(f"Saldo restante: {saldo_restante:.2f}")
            break
        elif saldo >= saque and saque < 0:
            print("Valor inválido para saque.")
            break
        elif saldo < saque:
            print("Saldo insuficiente.")
            break
    except:
        print("ERRO. DIGITE APENAS NÚMEROS.")
            