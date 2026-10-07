def soma (n1,n2:int):
    re  = n1 + n2
    return re
def Multiplicação(n1,n2:int):
    re = n1 * n2
    return re
def ler():
    num = int(input("Digite o número: "))
    return num
#Prog Principal
num1 = ler()
num2 = ler()
es = input("""A - Adição 
M - Multiplicação
Digite a sua escolha: """).upper()
if es == "A":
    resultado = soma(num1,num2)
    print(resultado)
elif es =="M":
    resultado = Multiplicação(num1,num2)
    print(resultado)
else:
    print("Invalido!!!")