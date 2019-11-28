



#def ultimo(num):
#    n = str(num)
#   ultimo = str.format(n[-1])
#    return ultimo

num = int(input("Digite um número inteiro terminado em ZERO: "))
lista = []

while num != 0:
    lista.append(num)
    num = int(input("Digite um número inteiro terminado em ZERO: "))

#    if ultimo(num) != 0:
#        print(input("O número deve terminar em ZERO! Digite novamente: "))

print(lista [::-1])