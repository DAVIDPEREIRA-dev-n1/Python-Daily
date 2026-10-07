def maior_menor(N:int):
    for i in range(1 , N+1):
        while True:
            nota = float(input("Digite a nota do {}º aluno (0 a 20): ".format(i)))
            if nota >= 0 or nota <= 20:
                break
            else:
                print("Nota inválida!")
        if i == 1:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
    print("A maior nota é: {}".format(maior))
    print("A menor nota é: {}".format(menor))
#Prog Principal
N = int(input("Digite o número de alunos: "))
maior_menor(N)


        
    





