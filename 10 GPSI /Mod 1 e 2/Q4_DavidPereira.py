def primo(x):
    if x >= 1:
        for i in range(1, x):
            if x % i != 0:
                print(x, 'é primo')
                break
            else:
                print(x, 'não é primo')
                break
    elif x == 0:
        print(x, 'é Invalido')
    else:
        print('o número tem que ser positivo')
#Prog Principal
n = int(input("Digite um numero: "))
primo(n)