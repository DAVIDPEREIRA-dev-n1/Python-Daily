def fatorial(n):
    if n == 0 or n == 1:
        return f"{n}! = 1"
    resultado = 1
    passos = []
    for i in range(n, 0, -1):
        resultado *= i
        passos.append(str(i))
    expressao = " * ".join(passos)
    return f"{n}! = {expressao} = {resultado}"
while True:
    try:
        numero = int(input("Digita um número inteiro positivo: "))
        
        if numero <= 0:
            print("Erro: O fatorial não está definido para números negativos ou 0.")
            continue  
        break
    except ValueError:
        print("Entrada inválida! Por favor, digita apenas números.")
print(fatorial(numero))