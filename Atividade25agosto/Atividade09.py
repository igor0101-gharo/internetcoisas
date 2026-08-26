import random

numero_secreto = random.randint(1,100)
tentativas = 0

while True:
    numero = int(input("Digite o Numero Secreto: \n"))
    tentativas+=1
    if numero == numero_secreto:
        print("Parabéns!! Você acertou o número")
        print(f"número de tentativas: {tentativas}")
    elif numero > numero_secreto:
        print("O número secreto é menor.")
        print(f"número de tentativas: {tentativas}")
    elif numero <  numero_secreto:
        print("O número secreto é maior.")
        print(f"número de tentativas: {tentativas}")
    