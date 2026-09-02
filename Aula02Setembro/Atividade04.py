import os 
os.system("cls")

lista_notas =[]
while True:
    try:
        lista_notas.clear()
        for i in range(3):
            nota = float(input(f"Digite a {i+1}ª nota: "))
            if nota >= 0 and nota <=10:
                lista_notas.append(nota)
            else:
                while True:
                    nota = float(input("Nota fora do permitido. Digite uma nota válida."))
                    if nota >= 0 and nota <=10:
                        lista_notas.append(nota)
                        break
        
        media = sum(lista_notas)/len(lista_notas)
        
        if media >=7:
            print(f" Média: {media:.2f}\n APROVADO.")
            break
        elif media >=5:
            print(f" Média: {media:.2f}\n RECUPERAÇÃO.")
            break
        else:
            print(f" Média: {media:.2f}\n REPROVADO.")
            break
    except:
        print("ERRO. DIGITE APENAS NÚMEROS.")
            
            