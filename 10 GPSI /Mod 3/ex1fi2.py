import math
def volume(x):
    r2 = (4/3) * math.pi * math.pow(x,3)
    return r2 
#Prog Principal
n = float(input("Digite o raio do circulo: "))
resultado = volume(n)
print("O volume da esfera é {:.2f} ".format(resultado))