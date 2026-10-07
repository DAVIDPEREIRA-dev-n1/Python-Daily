vetor = [0] * 10
soma = 0
for i in range(0,10):
    n = float(input("Digite um número real: ")) 
    vetor[i] = n 
    soma += n 
print(f"A soma é {soma:.2f}")