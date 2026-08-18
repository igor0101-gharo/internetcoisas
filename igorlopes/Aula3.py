numeros = [33,11,22,54,51,52,17]
nomes = ["julia","Maria","Luiza","Enzo"]

numeros.append(67)
numeros.insert(3,50)

print (numeros)

print(nomes)

print(nomes[2])

numeros.pop() #apaga o valor da ultima posição

print(numeros)

numeros.pop(2) #apaga o valor da posição indicada

print(numeros)

numeros.remove(51) #apaga o valor especificado

print(numeros)

nomes.remove("Enzo")

print(nomes)


#append - Insere um novo valor no vetor, sempre na última posição
#insert - Insere um novo valor no vetor em uma posição especifica. digita primeiro a posição e depois o valor
#pop - remove um valor de acordo com a posição.
#remove - remove um valor de acordo com a informação do valor.
#sort 
#reverse
#len
#count
#sum()
#max - #min