vetor = [0] * 10 
mn = 999999999999999999999999999999999999999999999999999999999999999999
for i in range(0,10):
    vetor[i] = n = float(input("Digite um número real: "))
    if n < mn :
        mn = n  
print(f"O menor número é {mn}")