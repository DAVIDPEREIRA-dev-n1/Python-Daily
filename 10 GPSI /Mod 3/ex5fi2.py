import math 
def fatorial(x):
    r = math.factorial(x)
    return r 
#Prog Principal 
n = int(input("Digite um número: "))
resultado = fatorial(n)
print("O fatorial é {:.2f} ".format(resultado))