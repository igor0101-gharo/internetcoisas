import os

lista_numeros = []
numeros_negativos = []
numeros_positivos = []

for i in range(10):
    numero=float(input(f"Digite o {i+1}º número:\n "))
    lista_numeros.append(numero)
    
os.system("cls")

for digito in lista_numeros:
    if digito < 0:
        numeros_negativos.append(digito)
    elif digito > 0:
        numeros_positivos.append(digito)
    


print(f"Quantidade de números negativos: {len(numeros_negativos)}")
print(f"Quantidade de números positivos: {len(numeros_positivos)}")
print(f"Vetor de números negativos: {numeros_negativos}")
print(f"Soma dos números positivos: {sum(numeros_positivos)}")
