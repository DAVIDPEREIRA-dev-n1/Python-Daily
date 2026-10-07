while True:
    def soma(n1, n2):
        return n1 + n2
    def subtracao(n1, n2):
        return n1 - n2
    def multiplicacao(n1, n2):
        return n1 * n2
    def divisao(n1, n2):
        if n2 != 0:
            return n1 / n2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return None
    n1 = float(input("Digite o primeiro número: "))
    escolha = input("Escolha a operação (+, -, *, /): ")
    n2 = float(input("Digite o segundo número: "))
    if escolha == '+':
        resultado = soma(n1, n2)
    elif escolha == '-':
        resultado = subtracao(n1, n2)
    elif escolha == '*':
        resultado = multiplicacao(n1, n2)
    elif escolha == '/':
        resultado = divisao(n1, n2)
    else:
        print("Operação inválida.")
        resultado = None
    if resultado is not None:   
        print("O resultado da operação é: ", resultado)
    vaiar = input("Deseja continuar? (s/n): ")
    if vaiar.lower() != 's':
        break
