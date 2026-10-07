def idade100(i:int):
    a = 2026-i
    id100=  a + 100
    return id100
#Prog Principal
nome = input("Digite o seu nome:") 
idade= int(input("Digite a idade sua idade no final deste ano: "))
cem = idade100(idade)
print(nome, "vai fazer 100 anos em ",cem)