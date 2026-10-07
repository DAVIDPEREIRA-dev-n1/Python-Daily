texto = input("Digite uma cadeia de caracteres: ")
caractere = input("Digite o caractere a procurar: ")
i = 0
posicao = -1
while i < len(texto):
    if texto[i] == caractere:
        posicao = i+1
        break
    i += 1
print("Posicao:", posicao)
