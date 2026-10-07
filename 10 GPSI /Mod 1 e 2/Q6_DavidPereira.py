def calcular_mdc(n1, n2):
    if n1 < n2:
        div = n1
    else:
        div = n2
    while n1 % div != 0 or n2 % div != 0:
        div = div - 1  
    print(f"O Máximo Divisor Comum é: {div}")
#Prog Principal
n1 = -1
n2 = -1
while True:
    n1 = int(input("Introduza o 1º número: "))
    n2 = int(input("Introduza o 2º número: "))
    if n1 == 0 and n2 == 0:
        break
    calcular_mdc(n1, n2)
