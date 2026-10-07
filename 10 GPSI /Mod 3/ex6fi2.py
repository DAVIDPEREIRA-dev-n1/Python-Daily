def calcular_media():
    soma = 0
    for i in range(30):
        temperatura = float(input("Digite a temperatura: "))
        soma = soma + temperatura
    media = soma / 30
    return media
# Prog principal
resultado = calcular_media()
print("Média das temperaturas:", format(resultado, ".2f"))