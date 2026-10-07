v = [0]*4
c = 0
for i in range(4):
    v[i] = float(input("Digite um número: "))
for i in range(4):
    if v[i] % 3 == 0 :
         c += 1 
print("Quantidade de números múltiplos de 3:", c)

