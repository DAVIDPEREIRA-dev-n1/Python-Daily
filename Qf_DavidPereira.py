frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
i = 0
contador = 0
while i < len(frase):
    if frase[i] in vogais:
        contador += 1
    i += 1
print("Número de vogais:", contador)
