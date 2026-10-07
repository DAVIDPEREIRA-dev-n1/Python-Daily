def ma (x,y:float):
    while True:
        x += 1
        n = float(input("Digita a sua nota(1 a 20): "))
        if n == 0 : 
            print("Invalido")
        y += n
        d  =input("Quer continuar a por notas(s/n): ").lower()
        if d == "n" :
            break
    m = y / x  
    print("A sua media aritmetica é {:.2f}".format(m)) 
#Programa Principal
i = 0
soma = 0 
ma(i,soma)