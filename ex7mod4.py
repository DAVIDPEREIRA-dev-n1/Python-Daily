letra = "s"
letra2 = "S"
frase = input("Digite uma frase: ")
c = 0
for i in range(0,len(frase)):
    if frase[i] == letra : 
        c = c + 1
    elif frase[i] == letra2 :
        c = c + 1
print("A sua letra aparece ",c," vezes na frase ")



