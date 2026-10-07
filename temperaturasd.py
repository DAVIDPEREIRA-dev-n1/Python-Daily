#saber ao longo de x dias qual mair temperatura e a menor e se repetir quero saber os dias que repetiu a temp 
vetor = []
maior = float('-inf')
menor = float('inf')
d = int(input("Quantos dias deseja inserir as temperaturas? "))
for i in range(d):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    vetor.append(temp)
    if temp > maior:
        maior = temp
        posicao = vetor[i]
    if temp < menor:
        menor = temp
print(f"A maior temperatura é {maior} e ocorreu no dia {vetor.index(maior)+1}")
print(f"A menor temperatura é {menor} e ocorreu no dia {vetor.index(menor)+1}")
