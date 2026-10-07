matriz = [[4,9], [1,21], [3,10]]
mn = 0 
l = 0 
c = 0
mn1 = 99999999999999999999999999999999999999999999999999999
l2 = 0
c2 = 0
mn2 = 99999999999999999999999999999999999999999999999999999
l3 = 0
c3 = 0
for i in range(3):
    for j in range(2):
        if j == 0:
             if matriz[i][j] < mn1:
                mn1 = matriz[i][j]
                l2 = i
                c2 = j
                print(f"O menor elemento da coluna 1 é {mn1} e está na linha {l2} e na posição ( {l2} ,{c2} )")
        if j == 1:
             if matriz[i][j] < mn2:
                mn2 = matriz[i][j]
                l3 = i
                c3 = j
                print(f"O menor elemento da coluna 2 é {mn2} e está na linha {l3} e na posição ( {l3} ,{c3} )")
        if matriz[i][j] > mn:
            mn = matriz[i][j]
            l = i
            c = j
print(f"O maior elemento é {mn} e está na linha {l} e na posição ( {l} ,{c} )")