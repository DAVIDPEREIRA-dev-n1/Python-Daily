def peso(x,y):
    if y.upper == "M":
        resulta = 72.7 * x - 58
        return resulta
    elif y.upper == "F":
        resulta = 62.1 * x - 44.7
        return resulta
    else: 
        print("Invalido")
#Prog Principal 
a = float(input("Digite a sua altura: "))
s = input("Digite o genero(M,F): ")
r = peso(a,s)
print("O seu peso ideal é {}".format(r))