v = []*4
mn = float("inf")
for i in range(4):
    v.append(float(input("Digite um número: ")))
    if v[i] < mn:
        mn = v[i]
