vetor = [0] * 10 
np = 0
for i in range(0,10):
    vetor[i] = n = float(input("Digite um número real: "))
    if n%2 == 0 :
        np += 1  
print(f"Tem {np} números pares.")