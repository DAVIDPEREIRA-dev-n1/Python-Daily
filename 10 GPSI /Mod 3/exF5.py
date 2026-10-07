import math
def primo(n):
    if n < 0 : 
        print("Invalido")
    for i in range(2, int(math.sqrt(n)) + +1):
        if n % i == 0:
            return False
    return True
# Prog Principal
num = int(input("Digite um número: "))
r = primo(num)
print(r)



