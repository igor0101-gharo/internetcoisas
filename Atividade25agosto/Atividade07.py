
import random

numeros = []
for i in range(100):
    numeros.append(i+1)
    
while True:    
    sorteado = random.choice(numeros)
    tentativas = 0

    while True:
        escolha = int(input("Tente adivinhar o número de 1 a 100."))
        
        if escolha > sorteado:
            print("O número é menor")
            tentativas = tentativas+1
        elif escolha < sorteado:
            print("O número é maior")
            tentativas = tentativas+1
        else:
            print("Você acertou o número!!")
            tentativas = tentativas+1
            print(f"número de tentativas: {tentativas}")
            break
    
    continuar = input("Quer sortear outro número?\nDigite sim para continuar ou qualquer outra coisa para encerrar. ").upper()
    if continuar != "SIM":
        break
    
            