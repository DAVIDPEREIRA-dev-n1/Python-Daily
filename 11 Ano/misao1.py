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

texto = input("Escreva uma palavra ou frase: ")
pilha_texto = Pilha()

for caractere in texto:
    pilha_texto.push(caractere)

texto_invertido = ""    
while not pilha_texto.is_empty():
    texto_invertido += pilha_texto.pop()

print("Texto invertido:", texto_invertido)
