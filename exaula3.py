matriz = [[0] * 4 for i in range(3)]
#soma = 0 
# mostrar a matriz
##for i in range(3):
 #   for j in range(4):
  #      x = float(input(f"Digite o valor para a posição ({i}, {j}): "))
   #     matriz[i][j] = x
    #    soma += x
for i in range (4):
    soma = 0
    for j in range (3):
        x = float(input(f"Digite o valor : "))
        matriz[i][j] = x
        print(matriz[i][j])
        soma += matriz[i][j]
    print(soma)
print(f"A soma dos elementos da matriz é: {soma}")

    



    
