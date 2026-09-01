import os
os.system("cls")

lista_numeros = []

for i in range(6):
    numero = float(input(f"\nDigite o {i+1}º número:\n"))
    lista_numeros.append(numero)

lista_numeros.sort()
print(f"Soma dos números: {sum(lista_numeros)}")
print(f"Maior valor: {max(lista_numeros)}")
print(f"Menor valor: {min(lista_numeros)}")
print(f"Número em ordem crescente: {lista_numeros}")