def par(n1, n2):
    resultado = n1 - n2
    if resultado > 0:
        print("A subtração é POSITIVA")
    elif resultado < 0:
        print("A subtração é NEGATIVA")
    else:
        print("A subtração é ZERO")
# Programa Principal
a = 1
b = 1
while a != 0 or b != 0:
    a = int(input("1º Número: "))
    b = int(input("2º Número: "))
    if a != 0 or b != 0:
        par(a, b)
    else:
        print("Encerramento")

