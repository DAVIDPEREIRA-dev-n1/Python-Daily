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
    

frase = input("Escreva uma frase: ")
p = Pilha()

for caractere in frase:
    p.push(caractere)

frase_invertida = ""
while not p.is_empty():
    frase_invertida += p.pop()

print("Frase invertida:", frase_invertida)

    