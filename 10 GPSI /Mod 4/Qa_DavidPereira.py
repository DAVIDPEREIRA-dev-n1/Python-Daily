letra = "s"
letra2 = "S"
frase = input("Digite um nome: ")
c = 0
c2 = 0
for i in range(0,len(frase)):
    if frase[i] == letra : 
        c += 1
    elif frase[i] == letra2 :
        c2 += 1
print("A letra S aparece ",c2," vezes no nome e a letra s aperece ", c ,"vezes na frase")