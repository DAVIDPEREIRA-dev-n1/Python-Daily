v = []*4
soma = 0 
for i in range(4):
    v.append(float(input("Digite um número: ")))
for i in range(4):
    soma += v[i]
print(v)
print("A soma dos números é:", soma)