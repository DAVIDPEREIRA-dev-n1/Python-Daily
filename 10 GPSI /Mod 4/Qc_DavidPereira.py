frase = input("Escreve uma frase: ")
palavra = ""
for i in range(len(frase)):
    if frase[i] != " ":
        palavra += frase[i]
    else:
        print(palavra)
        palavra = ""
if palavra != "":
    print(palavra)