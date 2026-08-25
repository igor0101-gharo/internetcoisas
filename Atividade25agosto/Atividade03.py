lista_nomes = []

for i in range(5):
    nome= input(f"Digite o {i+1}º nome:\n ")
    lista_nomes.append(nome)
    
lista_nomes.sort()

print(lista_nomes)