def obter_palavra():
    palavra = input("Digite a sua Palavra: ")
    return palavra
def palavras_iguais(p1, p2):
    if p1 == p2:
        return True
    else:
        return False
# Prog principal
palavra1 = obter_palavra()
palavra2 = obter_palavra()
if palavras_iguais(palavra1, palavra2):
    print("As palavras são iguais")
else:
    print("As palavras não coincidem")