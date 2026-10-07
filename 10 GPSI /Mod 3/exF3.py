def Par(x):
    if x % 2 == 0 :
        return True 
    else :
        return False 
#Prog Principal
n = int(input("Digite um número para descobrir se e par: "))
r = Par(n)
print(r)