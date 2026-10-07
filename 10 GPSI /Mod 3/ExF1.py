def PN(x):
    if x > 0 :
        return True 
    elif x < 0 : 
        return False 
#Prog Principal
n = int(input("Digite um número: "))
r = PN(n)
print(r)