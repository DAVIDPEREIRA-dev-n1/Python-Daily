palavra = input("Digite uma palavra: ") 
tamanho = len(palavra)  
#while i >= 0:
for i in range(tamanho-1,-1,-1):
    print(palavra[i], end="")


