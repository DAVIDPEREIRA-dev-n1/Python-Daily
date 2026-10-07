nome ={"nome":"David","Idade":18}
vetor = []
vetor.append(nome["nome"])
vetor.append(nome["Idade"])
for i in range(1,4):
    nome["Idade"] = int(input("Digite a idade: "))
    nome["nome"] = input("Digite o nome: ")
    vetor.append(nome["nome"])
    vetor.append(nome["Idade"])
    print(nome)            
print(vetor)