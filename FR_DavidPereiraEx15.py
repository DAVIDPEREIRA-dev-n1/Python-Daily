linha = 5
coluna = 3 
soma = 0
matriz = [[0 for c in range(coluna)] for l in range(linha)]
for i in range(0, linha):
    for c in range(0, coluna):
        matriz[i][c] = float(input(f"Digite o valor para ({i}, {c}): "))
        soma += matriz[i][c]
print(matriz)   
print(f"A soma dos elementos da matriz é: {soma}")
