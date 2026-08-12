idade = int(input("Digite a sua idade: "))

if idade < 18 and idade > 0:
    print("você é menor de idade.")
elif idade >= 18:
    print("você é maior de idade.")
else: 
    print("valor inválido.")