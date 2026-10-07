class Pilha:
    def __init__(self):
        self.elements = []

    def push(self, valor):
        self.elements.append(valor)

    def is_empty(self):
        return len(self.elements) == 0 

    def pop(self):
        if  self.is_empty():
            return None
        return self.elements.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def show(self):
        return self.elements
    
#Programa principal


numero = int(input("Escreva um número decimal inteiro não negativo: "))
pilha_binario = Pilha()

if numero < 0:
    print("O número tem de ser não negativo.")
elif numero == 0:
    pilha_binario.push(0)
else:
    while numero > 0:
        resto = numero % 2
        pilha_binario.push(resto)
        numero = numero // 2

binario = ""
while not pilha_binario.is_empty():
    binario += str(pilha_binario.pop())

if binario:
    print("Representação binária:", binario)
    