alunos = int(input("Digite o número de alunos: "))
soma_notas = 0
for i in range(alunos):
    nota = float(input("digite a nota do aluno : "))
    soma_notas += nota
media = soma_notas / alunos
print("A média das notas é: ", media)