vetor=[0] * 12
c = 0
for i in range(12):
    vetor[i] = float(input("Digite um número : "))
    if vetor[i] % 3 == 0:
        c +=1
print(f"Existem {c} números que são divisíveis por 3.")