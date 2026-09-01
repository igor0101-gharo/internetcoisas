import os
os.system("cls")

lista_notas = []

while True:
    nota = float(input("\nDigite a próxima nota(digite -1 para sair):\n"))
    if nota == -1:
        break
    else:
        lista_notas.append(nota)
        
print("===LISTA DE NOTAS===")
for notas in lista_notas:
    print(f"-{notas}")

media = sum(lista_notas)/len(lista_notas)

print(f"\n\nQuantidade de notas cadastradas: {len(lista_notas)}")
print(f"Média: {media}")
print(f"Maior nota {max(lista_notas)}")
print(f"menor nota {min(lista_notas)}")

lista_notas.sort()
lista_notas.reverse()

print(f"Notas em ordem decrescente: {lista_notas}")