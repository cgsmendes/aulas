peso = float(input("Qual o peso em quilos: "))
if peso > 50:
    excessopeso = peso - 50
    print("Você excedeu o peso limite em: ",excessopeso,"!")
    multa = excessopeso * 4
    print("A multa é de R$ 4,00 por quilo excedente, neste caso você deverá pagar um total de: R$ ",multa," de multa!")
else:
    print("Você está dentro do limite permitido de até 50 quilos. Peso atual é de: ",peso)