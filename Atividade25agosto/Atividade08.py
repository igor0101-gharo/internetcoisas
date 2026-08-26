numeros =[]
import random


quantidade_numeros = int(input("digite a quantidade de números."))
for i in range(quantidade_numeros):
    numeros.append(i+1)
    
sorteado1 = random.choice(numeros)
sorteado2 = random.choice(numeros)
escolha1 = 0
escolha2 = 0
tentativas1 = 0
tentativas2 = 0
quantidade_jogadores= int(input("Digite o número de jogadores. (1 ou 2)")) 

match quantidade_jogadores:
    case 1:
        while True:
            escolha1 = int(input(f"Tente adivinhar o numero de 1 a {quantidade_numeros}:\n"))
            if escolha1 > sorteado1:
                tentativas1+=1
                print("O número sorteado é menor")
            elif escolha1 < sorteado1:
                tentativas1+=1
                print("o número sorteado é maior")
            else:
                tentativas1+=1
                print("você acertou!!")
                print(f"Número de tentativas:{tentativas1}")
                break
                
    case 2:
        quantidade_sorteio = int(input("os jogadores vão tentar adivinhar o mesmo número ou numeros diferentes? digite 1 ou 2\n"))
        match quantidade_sorteio:
                case 1:
                    while True:
                        escolha1 = int(input("Jogador 1 tente adivinhar o número:\n"))
                        if escolha1 > sorteado1:
                            print("O número é menor.")
                            tentativas1 += 1
                        elif escolha1 < sorteado1:
                            print("O número é maior.")
                            tentativas1 += 1
                        else:
                            tentativas1 += 1
                            print("O jogador 1 acertou o número.")
                            print(f"Número de tentativas do jogador 1: {tentativas1}")    
                            print(f"Número de tentativas do jogador 2: {tentativas2}")
                            break    
            
                        
                        escolha2 = int(input("Jogador 2 tente adivinhar o número:\n"))
                        if escolha2 > sorteado1:
                            print("O número é menor.")
                            tentativas2 += 1
                        elif escolha2 < sorteado1:
                            print("O número é maior.")
                            tentativas2 += 1
                        else:
                            tentativas2 += 1
                            print("O jogador 2 acertou o número!")
                            print(f"Número de tentativas do jogador 1: {tentativas1}")    
                            print(f"Número de tentativas do jogador 2: {tentativas2}")
                            break    
        
                case 2:
                    while True:
                        escolha1 = int(input("Jogador 1 tente adivinhar o seu número:\n"))
                        if escolha1 > sorteado1:
                            print("O número é menor.")
                            tentativas1 += 1
                        elif escolha1 < sorteado1:
                            print("O número é maior.")
                            tentativas1 += 1
                        else:
                            tentativas1 += 1
                            print("O jogador 1 acertou o número.")
                            print(f"Número de tentativas do jogador 1: {tentativas1}")    
                            while True:
                                escolha2 = int(input("Jogador 2 tente adivinhar o seu número:\n"))
                                if escolha2 > sorteado2:
                                    print("O número é menor.")
                                    tentativas2 += 1
                                elif escolha2 < sorteado2:
                                    print("O número é maior.")
                                    tentativas2 += 1
                                else:
                                    tentativas2 += 1
                                    print("O jogador 2 acertou o número!")
                                    print(f"Número de tentativas do jogador 2: {tentativas2}")
                                    break
                    
                        if escolha2 == sorteado2:
                                break
                        
                        
                        escolha2 = int(input("Jogador 2 tente adivinhar o seu número:\n"))
                        if escolha2 > sorteado2:
                            print("O número é menor.")
                            tentativas2 += 1
                        elif escolha2 < sorteado2:
                            print("O número é maior.")
                            tentativas2 += 1
                        else:
                            tentativas2 += 1
                            print("O jogador 2 acertou o número!")
                            print(f"Número de tentativas do jogador 2: {tentativas2}")
                            while True:
                                escolha1 = int(input("Jogador 1 tente adivinhar o seu número:\n"))
                                if escolha1 > sorteado1:
                                    print("O número é menor.")
                                    tentativas1 += 1
                                elif escolha1 < sorteado1:
                                    print("O número é maior.")
                                    tentativas1 += 1
                                else:
                                    tentativas1 += 1
                                    print("O jogador 1 acertou o número.")
                                    print(f"Número de tentativas do jogador 1: {tentativas1}")
                                    break
                        break
                                
                                    
                    
                    
                case _:
                    print("valor inválido. digite novamente.")
    case _:
        print("valor inválido.")
    