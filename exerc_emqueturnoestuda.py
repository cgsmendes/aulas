letra = str(input("Digite M, V ou N: "))

if letra is 'm' or letra is 'M':
    print(letra, "Bom dia!")
elif letra is 'v' or letra is 'V':
    print(letra, "Boa tarde!")
elif letra is 'n' or letra is 'N':
    print(letra, "Boa noite!")
else:
    print("VALOR INVÁLIDO!")