numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


distancia = (numero1-numero2)**2
modulo = distancia**(1/2)

resultado = (numero1+numero2)/2 + modulo/2

print(resultado)