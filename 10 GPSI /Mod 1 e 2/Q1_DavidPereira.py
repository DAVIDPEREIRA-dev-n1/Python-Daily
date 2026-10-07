def soma(y:int):
   for  i in range (0,n):
      n2 = int(input("digite um numero: "))
      y += n2 
   media(y)   
def media(y:int):
   m = y/n
   print("A media é {:.2f}".format(m))
#Prog Principal
n = int(input("Digite a quantidade de números para somar : "))
s = 0
soma(s)
