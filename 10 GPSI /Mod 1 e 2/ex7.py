n = int(input("Digite um número entre 3 e 8: "))
match n:
  case 3:
    print("Triângulo equilátero")
  case 4:
    print("Quadrado")
  case 5:
    print("Pentágono")
  case 6:
    print("Hexágono")
  case 7:
    print("Heptágono")
  case 8:
    print("Octógono")
  case _:
    print("Invalido, digite um número entre 3 e 8 ")
