def imc(x,y:float):
    mc = x/(y**2)
    print("O seu IMC é {:.2f} ".format (mc))
    if mc < 18.50:
        print("Baixo peso")
    elif mc <= 24.9 :
        print("Peso Normal")
    elif mc <= 29.9 :
        print("Pre Obesidade")
    elif mc <= 34.9 :
        print("Obesidade grau 1")    
    elif mc <= 39.9:
        print("Obesidade grau 2") 
    elif mc >= 40:
        print("Obesidade grau 3")    

p = float(input("Digite o peso(kg): "))     
a = float(input("Digite a altura(m): "))  
imc(p,a)

    
