uni1 = float(input("Digite a nota da primeira unidade: "))
uni2 = float(input("Digite a nota da segunda unidade: "))
uni3 = float(input("Digite a nota da terceira unidade: "))

media = (uni1 + uni2 + uni3) / 3

print(f"Sua média é {media:.1f}")
if media >= 7:
    print("parabéns, você foi aprovado!")
elif media < 7:
    print("você está de recuperação!")