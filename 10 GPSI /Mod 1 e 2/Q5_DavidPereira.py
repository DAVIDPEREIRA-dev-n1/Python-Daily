def calcular_mmc(n1, n2):
    if n1 < n2 :
        maior = n2
    else:
        maior = n1
    mmc = maior
    while mmc % n1 != 0 or mmc % n2 != 0:
        mmc = mmc + maior       
    return mmc
#Prog Principal
n1 = -1
n2 = -1
while n1 != 0 or n2 != 0:
    n1 = int(input("Introduza o 1º número: "))
    n2 = int(input("Introduza o 2º número: "))
    if n1<0 or n2<0 : 
        print("invalido")
        break
    if n1 != 0 or n2 != 0:
        resultado = calcular_mmc(n1, n2)
        print("O mínimo múltiplo comum de ",n1,"e ",n2," é :", resultado)


