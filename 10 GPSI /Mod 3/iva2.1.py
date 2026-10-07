def iva(x:float,y:int):
    match y :
        case 1  :
            resultado = (x * 0.23) + x 
            return resultado
        case 2 :
            resultado = (x * 0.13) + x 
            return resultado
        case 3 :
            resultado = (x * 0.06) + x 
            return resultado
        case _:
            return "Invalido"
#Prog Principal 
p = float(input("Digite o preço: "))
i = int(input("Digite o nivel do iva: "))
r =iva(p,i)
print("O preço do iva é ",r)