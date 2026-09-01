import os
os.system("cls")

lista_produtos =[]
for i in range(5):
    produto = input(f"\nDigite o {i+1}º produto:\n ")
    lista_produtos.append(produto)

print("====LISTA DE PRODUTOS====")
for item in lista_produtos:
    print(item)
    
print(f"Quantidade de produtos: {len(lista_produtos)}")