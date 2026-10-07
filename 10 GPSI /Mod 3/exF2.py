import math
def raio(x):
    r2 = math.sqrt(x / (4 * math.pi))
    return r2 
#Prog Principal
n = float(input("Digite a área do circulo: "))
resultado = raio(n)
print("O raio do esfera é {:.2f} ".format(resultado))
