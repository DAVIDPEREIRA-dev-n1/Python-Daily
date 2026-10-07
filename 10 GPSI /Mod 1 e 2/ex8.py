def figuras(x:int):
    if x == 3:
        print("Triângulo equilátero")
    elif x == 4:
        print("Quadrado")
    elif x == 5:
        print("Pentágono")
    elif x == 6:
        print("Hexágono")
    elif x == 7:
        print("Heptágono")
    elif x == 8:
        print("Octógono")
    else:
        print("Invalido, digite um número entre 3 e 8 ")
#Programa Principal
n = int(input("Digite um número entre 3 e 8: "))
figuras(n)
