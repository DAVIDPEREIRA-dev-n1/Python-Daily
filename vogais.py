#determine a quantidade de vogais 
n = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = sum(1 for letra in n if letra in vogais)
print("Tem ",contador,"vogais")