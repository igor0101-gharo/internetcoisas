#for

#while - laço infinito

for i in range(3):#roda 3 vezes (de 0 a 2)
    print("Lucas")
    
import os
carrinho = []

while True:
    os.system("cls")
    produto = float(input("Digite o valor do produto: "))
    if produto== 0:
        break
    else:
        carrinho.append(produto)
        
print(f"Valor da compra: R${sum(carrinho):.2f}")