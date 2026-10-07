def iva(x:float,y:int):
    if y == 1 :
        resultado = (x * 0.23) + x 
        return resultado
    if y == 2 :
        resultado = (x * 0.13) + x 
        return resultado
    if y == 3 :
        resultado = (x * 0.06) + x 
        return resultado
#Prog Principal 
p = float(input("Digite o preço: "))
i = int(input("Digite o nivel do iva: "))
r =iva(p,i)
print("O preçocom iva é ",r)