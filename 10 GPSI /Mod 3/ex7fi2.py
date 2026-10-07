import math
def ler(men):
    valor = float(input(men))
    return valor
def obter_quadrado(a, b):
    return (a - b) ** 2
# programa principal
x1 = ler("Introduza x1: ")
y1 = ler("Introduza y1: ")
x2 = ler("Introduza x2: ")
y2 = ler("Introduza y2: ")
distancia = math.sqrt(obter_quadrado(x2, x1) + obter_quadrado(y2, y1))
print("Distância entre os pontos:", format(distancia, ".2f"))