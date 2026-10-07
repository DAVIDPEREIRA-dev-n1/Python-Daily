#Iniciar o vetor 
vetor = []
soma = 0
i = 0
while  True:
    m = float(input("Insira o valor: "))
    vetor.append(m)
    soma += vetor[i]
    i += 1
    if i == 3:
        break
    
    
print(vetor)


