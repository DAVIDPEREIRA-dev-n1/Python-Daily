def idade(dias,meses,anos):
    idt = ( meses * 30 ) + (anos * 365) + dias
    return idt
#Prog Principal
d = int(input("Digite os Dias: "))
m = int(input("Digite os Meses: "))
a = int(input("Digite os Anos: "))
resultado = idade(d,m,a)
print("Voçe tem ", resultado,"dias.")