import os
os.system("cls")

lista_convidados = []
convidado = ""

while True:
    convidado = input("\nDigite o nome do convidado(digite 'fim' para sair):\n")
    if convidado == "fim":
        break
    else:
        lista_convidados.append(convidado)

lista_convidados.sort()

print("====LISTA DE CONVIDADOS===")
for item in lista_convidados:
    print(item)
print(f"Quantidade de convidados: {len(lista_convidados)}")