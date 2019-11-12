areapintada = round((float(input("Digite o tamanho da área a ser pintada (em metros quadrados): ")) * 1.1), 2)
print("areapintada =", areapintada)
litros = round((areapintada / 6), 2)
print("litros =", litros)
lata18 = litros // 18
print("lata18 =", lata18)
resto18 = round((litros % 18), 2)
print("resto18 =", resto18)
lata36 = litros // 3.6
print("lata3,6 =", lata36)
resto36 = round((litros % 3.6), 2)
print("resto3,6 =", resto36)

valor18 = lata18 * 80
valor36 = lata36 * 25

if resto18 > 0:
    lata181 = lata18 + 1
    valor181 = lata181 * 80
    print("Você precisa de", lata181, "latas de tinta de 18 litros no valor total de R$", valor181)
else:
    print("Você precisa de", lata18, "latas de tinta de 18 litros no valor total de R$", valor18)

if resto36 > 0:
    lata361 = lata36 + 1
    valor361 = lata361 * 25
    print("Você precisa de", lata361, "latas de tinta de 3,6 litros no valor total de R$", valor361)
else:
    print("Você precisa de", lata36, "latas de tinta de 3,6 litros no valor total de R$", valor36)

if lata181 > 1 and resto18 > 0:
    lata36total = resto18 // 3.6
    restolata36total = resto18 % 3.6
    if restolata36total > 0:
        lata36total = lata36total + 1
        valor36 = lata36total * 25
    print("Você precisa de", lata18, "latas de 18 lts e mais", lata36total, "latas de 3,6 lts, no valor total de R$", valor36 + valor18)