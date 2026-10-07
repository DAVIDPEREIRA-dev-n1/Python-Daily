vetor =[0]* 8
for i in range(8):
    vetor[i] = float(input("Digite um número: "))
    if i == 0:
        mn = vetor[i]
    if vetor[i] < mn:
        mn = vetor[i]
print(f"O menor número digitado foi: {mn}")