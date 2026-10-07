vetor = [0] * 10
print(vetor)
for i in range(0,10):
    n = int(input("Digite um número inteiro: "))
    vetor[i] = n
#ex3
for i in range(0,len(vetor)):
    print(i, "-",vetor[i])