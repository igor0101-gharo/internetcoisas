import random
lista_nomes = []

for i in range(10):
    nome= input(f"Digite o {i+1}º nome:\n ")
    lista_nomes.append(nome)

nome_escolhido = random.choice(lista_nomes)

print(f"Nome sorteado: {nome_escolhido}")