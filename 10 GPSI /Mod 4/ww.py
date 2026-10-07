linha = 4 
coluna = 3 
soma = 0
matriz = [0 for i in range(4) for j in range (3)]
for i in range(0,linha):
    for c in range(0,coluna):
        matriz[i][c] = 0    
    print(matriz)
for i in range(0,linha):
    for c in range(0,coluna):
        matriz[i][c]= int(input(f"Digite o valor para a posição ({i}, {c}): "))
        soma += matriz[i][c]
print(matriz)   
print(f"A soma dos elementos da matriz é: {soma}")
#somar os elementos da matriz