n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

if 10 > (n1 + n2)/2 >= 7:
    print("Aprovado")
elif (n1 + n2)/2 < 7:
    print("Reprovado")
else:
    print("Aprovado com Distinção!")