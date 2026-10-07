nome = input("Digite um nome: ")
c = 0 
for i in nome:
    if i == "a" :
        c += 1
print(f"O nome {nome} tem {len(nome)} caracteres no total.")
print(f"O nome {nome} contém {c} ocorrências da letra 'a'.")
