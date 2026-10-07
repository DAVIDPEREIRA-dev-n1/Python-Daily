def notas(x,x2,x3,x4,y,z:float,l:str):
    y = (x+x2+x3+x4)/4
    x = ((x * 2)/15) + ((x2 * 3)/15) + (( x3 * 4)/15) + ((x4 * 6)/ 15)
    if l == "A" : 
        print("A media aritmetica é ", y )
    elif l == "P" :
        print(" A media ponderada é", x)
    else:
        print("Invalido")
    print("A media aritmetica é ", y ,"e a media ponderada", x )

#Programa principal
n = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))
n3 = float(input("Digite a 3º nota: "))
n4 = float(input("Digite a 4º nota: "))
letras =input("Digite a media que quer(A ou P ): ")
m = 0
p = 0
notas(n,n2,n3,n4,m,p,letras)