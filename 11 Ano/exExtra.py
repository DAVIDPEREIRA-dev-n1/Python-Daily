lista_alunos = []

n = int(input("Quantos alunos deseja registar? "))
soma = 0

for i in range(n):

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    lista_alunos.append(aluno)
    
for aluno in lista_alunos:
    if aluno["nota"] >= 10:
      soma += 1

print(f"Número de alunos aprovados: {soma}")



