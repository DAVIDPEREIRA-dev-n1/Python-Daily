def PI(x):
    if x % 2 == 0 :
        r = "Par"
    else :
        r = "Impar"
    return r
#Prog Principal
n = int(input("Digite um número : "))
resultado = PI(n)
print(resultado)