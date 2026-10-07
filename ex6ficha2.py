vetor = [0] *10 
man = -999999999999999999999999999999999999999999999999999999999999999999
for i in range(0,10):
    vetor[i] = n = float(input("Digite um número real: "))
    if n < man :
        man = n  
print(f"O maior número é {man}")