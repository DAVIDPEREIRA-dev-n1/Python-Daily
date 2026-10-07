#Determine com base de um texto  a palabra com mairo comprimento
n = input("Digite um texto: ")
palavras = n.split()
mp = max(palavras,key=len)
print("A maior palavra é ",mp)

     