n = 5
d = [None] * n
media = 0.0
maior = 0.0
menor = 21.0
qa = 0 
qr = 0
print("==========Introducao dos dados==========")
for i in range(n):
    print(f"Aluno nº {i+1} ")
    d[i] = {"nome": "", "idade": 0, "nota": 0.0}
    d[i]["nome"] = input("Digite o nome do aluno: ")
    d[i]["idade"] = int(input("Digite a idade do aluno: "))
    if d[i]["idade"] > 130:
        print("Idade inválida. Digite uma idade entre 0 e 130.")
        d[i]["idade"] = int(input("Digite a idade do aluno: "))
    d[i]["nota"] = float(input("Digite a nota do aluno: "))
    media += d[i]["nota"]
    if d[i]["nota"] > maior:
        maior = d[i]["nota"]
    if d[i]["nota"] < menor:
        menor = d[i]["nota"]
    if d[i]["nota"] < 0 or d[i]["nota"] > 20:
        print("Nota inválida. Digite uma nota entre 0 e 20.")
        d[i]["nota"] = float(input("Digite a nota do aluno: "))
        if d[i]["nota"] < 10 :
            qr += 1
        elif d[i]["nota"] >= 10 :
            qa += 1
proposta = input("Digite o Nome do aluno a encontrar: ")
encontrado = False
if proposta == "" or proposta == int or proposta == float:
    input("Nome inválido. Digite um nome válido:")
    for i in range(n):
        if d[i]["nome"] == proposta:
            encontrado = True
            print(f"Aluno encontrado: Nome: {d[i]['nome']},posicao: {i}")
for i in range(n):
    if d[i]["nome"] == proposta:
        print(f"Aluno encontrado: Nome: {d[i]['nome']}, Idade: {d[i]['idade']}, Nota: {d[i]['nota']}")
        encontrado = True
if  encontrado == False:
    print("Aluno não encontrado.")
elif encontrado == True:
    print("Aluno encontrado com sucesso.")
print("==========Dados dos alunos==========")
for i in range(n):
    print(f"====Aluno nº {i+1}====")
    print(f"Nome: {d[i]['nome']}, Idade: {d[i]['idade']}, Nota: {d[i]['nota']} )")
for i in range(n-1):
    pos_mim = i
    for j in range(i+1, n):
        if d[j]["nota"] < d[pos_mim]["nota"]:
            pos_mim = j
    if pos_mim != i:
        aux = d[i]
        d[pos_mim] = aux
print("==========Dados dos alunos ordenados por nota==========")
for i in range(n):
    print(f"====Aluno nº {i+1}====")
    print(f"Nome: {d[i]['nome']}, Idade: {d[i]['idade']}, Nota: {d[i]['nota']} )")
print(f"Media das notas: {media/n}")
print(f"Menor nota: {menor}")
print(f"Maior nota: {maior}")
print(f"Quantidade de alunos aprovados: {qa}")
print(f"Quantidade de alunos reprovados: {qr}")