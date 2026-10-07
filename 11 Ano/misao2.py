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

expressao = input("Escreva uma expressão: ")
pilha_parenteses = Pilha()
parenteses_validos = True

for caractere in expressao:
    if caractere == "(":
        pilha_parenteses.push(caractere)
    elif caractere == ")":
        if pilha_parenteses.is_empty():
            parenteses_validos = False
            break
        pilha_parenteses.pop()

if parenteses_validos and pilha_parenteses.is_empty():
    print("VÁLIDO: os parênteses estão equilibrados.")
else:
    print("INVÁLIDO: os parênteses não estão equilibrados.")
