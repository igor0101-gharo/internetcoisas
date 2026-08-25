lista_notas=[]
notas_acima=[]

for i in range(8):
    nota = float(input(f"Digite a {i+1}ª nota: \n"))
    lista_notas.append(nota)
    
media = sum(lista_notas)/len(lista_notas)

for notas in lista_notas:
    if notas > media:
        notas_acima.append(notas)
        
print(f"Média da turma: {media}")
print(f"Notas acima da média: {notas_acima} ")
