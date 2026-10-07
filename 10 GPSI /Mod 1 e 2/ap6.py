def media(i,x:int):
    y = int(input("Digite um número de repeticoes para somar: "))
    i = 0
    x = 0
    for i in range (0,y):
        n = int(input("Digie um número: "))
        i += 1
        x += n
    y = x / y
    print("A média é {:.2f} ".format(y))

#Prog Principal
c = 0
soma = 0
media(c,soma)
