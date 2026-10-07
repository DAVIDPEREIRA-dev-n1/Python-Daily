matriz = [[4,9], [1,21], [3,10]]
for i in range(2):
    mn1 = 999999999999999999999
    for j in range(3):
        if (matriz[j][i] < mn1):
            mn1 = matriz[j][i]
            l2 = j
            c2 = i
    print(f"O menor elemento da coluna 1 é {mn1} e está na linha {l2} e na posição ( {l2} ,{c2} )")
        