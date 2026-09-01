import os
os.system("cls")

import random

numero_secret = random.randint(1,20)

while True:
    escolha = int(input("\nDigite o seu palpite:\n"))
    
    if escolha == numero_secret:
        print("\n\nParabéns! você acertou!")
        break
    elif escolha < numero_secret:
        print("\n\nPalpite incorreto. O número secreto é MAIOR")
    elif escolha > numero_secret:
        print("\n\nPalpite incorreto. O número secreto é MENOR")
    