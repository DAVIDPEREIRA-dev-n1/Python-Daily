def calculo_imc(a, p):
    imc = p / (a ** 2)
    return imc
def classif(valor):
    if valor > 0 and valor < 18.5:
        return "Baixo peso"
    elif valor >= 18.5 and valor < 25:
        return "Peso Normal"
    elif valor >= 25 and valor < 30:
        return "Pré-obesidade"
    elif valor >= 30 and valor < 35:
        return "Obesidade Grau 1"
    elif valor >= 35 and valor < 40:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"
#Prg Principal
peso = float(input("Indique o seu peso em Kg: "))
altura = float(input("Indique a sua altura em metros: "))
imc = calculo_imc(altura, peso)
categoria = classif(imc)
print(f"IMC = {imc:.2f}")
print(categoria)