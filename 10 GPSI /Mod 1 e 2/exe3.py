def medias (n1,n2,n3,n4:float,m:str):
    match m :
          case "A": 
             media = (n1 + n2 +n3 + n4) /4
          case "P": 
                media =(2*n1 + 3*n2 + 4 *n3 + 5*n4)/4
          case _:
              media = 0
    return media
#Prog Principal 
resultado = medias(5,8,7,8,"A")
print("O resultado é: ", resultado)
resultado = medias (8,7,7,8,"P")
print("O resultado é :" , resultado)

