texto = input("Escreve uma frase: ") + " "
maior = ""
atual = ""
for letra in texto:
    if letra != " ":
        atual += letra
    else:
        if len(atual) > len(maior):
            maior = atual
        atual = ""
print("A maior palavra é:", maior)
