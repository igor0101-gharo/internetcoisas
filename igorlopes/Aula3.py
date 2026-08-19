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

numeros.sort()
nomes.sort()
print (numeros)
print(nomes)

numeros.reverse()
print (numeros)

quantidade = len(numeros)

print(f"a quantidade de números é {quantidade}")

numeros.append(11)

print(numeros.count(11)) #também pode ser colocada numa varivel Exemplo: quantidade = numeros.count(11)

soma = sum(numeros)
print(soma)

print(f"Maior número: {max(numeros)}") #também pode ser colocada numa variavel Exemplo: maior = max(numeros)
print(f"Menor número: {min(numeros)}")


#append - Insere um novo valor no vetor, sempre na última posição
#insert - Insere um novo valor no vetor em uma posição especifica. digita primeiro a posição e depois o valor
#pop - remove um valor de acordo com a posição.
#remove - remove um valor de acordo com a informação do valor.
#sort - coloca o vetor em ordem crescente ou ordem alfabética.
#reverse - inverte a ordem do vetor. 
#len - Informa quantos valores existem dentro de um vetor.
#count - conta quantos de um valor especifico existem num vetor.
#sum() - Soma todos os valores de um vetor.
#max - Informa o maior valor dentro de um vetor 
#min - Informa o menor valor dentro de um vetor