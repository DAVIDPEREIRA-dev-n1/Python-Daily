def area(B,b,h):
    resultado = ((B + b)*h)/2
    return resultado
#Prog Principal
bM = int(input("Digite a Base Maior: "))
Bm = int(input("Digite a Base Menor: "))
a = int(input("Digite a Altura: "))
r = area(bM,Bm,a)
print("A área é {:.2f}".format(r))