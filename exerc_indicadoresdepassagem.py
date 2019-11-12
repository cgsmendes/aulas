meuCartao = int(input("Digite o número do seu cartão: "))

cartaoLido=1
encontreiMeuCartaoNaLista = False

while cartaoLido !=0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print("EBA! Meu cartão está na lista!")
else:
    print("Xi, meu cartão não está na lista!")