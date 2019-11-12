areapintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))
if areapintada > 54:
    litros = areapintada // 3
    restolitros = areapintada % 3
    lata = litros // 18
    valor = lata * 80
    if restolitros > 0:
        lata = lata + 1
        valor = lata * 80
        print("Você precisa de ", lata, " latas de tinta lata de tinta no valor total de R$ ", valor)
    else:
        print("Você precisa de ", lata, " latas de tinta lata de tinta no valor total de R$ ", valor)
else:
    print("Você só precisa de 1 lata de tinta no valor total de R$ 80,00.")