def soma_pares(lista):
    contador_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            contador_pares += 1
    return contador_pares

n = int(input("Quantos números deseja inserir na lista? "))

lista_numeros = []

for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

quantidade_pares = soma_pares(lista_numeros)

print(f"Quantidade de números pares na lista: {quantidade_pares}")




