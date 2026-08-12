temperatura = float(input("Digite a temperatura"))

if temperatura < 15:
    print("está frio.")
elif temperatura >=15 and temperatura <= 25:
    print("Está agradável.")
elif temperatura > 25:
    print("está quente.")