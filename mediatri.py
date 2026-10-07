#Iniciar o vetor 
vetor = [0] * 3
soma = 0
#iniciar um ciclo para pedir o valor
for i in range(0,3):
    m = float(input("Insira o valor gasto em transporte no mês: "))
    soma += m
    vetor[i]=m
media = soma/len(vetor)
print("A Valor gasto é: ",soma)
print("A Media Trimestral do Valor gasto é: ",media)
print("O Valor do 1ºMês é:",vetor[0])
print("O Valor do 2ºMês é:",vetor[1])
print("O Valor do 3ºMês é:",vetor[2])
