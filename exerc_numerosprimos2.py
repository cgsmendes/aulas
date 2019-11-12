def primo(x):
    fator = 2
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0 and x != 2:
        return False
    else:
        return True

n = int(input("Digite um número inteiro maior que 0: "))

while n > 0:
    if primo(n):
        print(n,"É PRIMO!")
    else:
        print(n, "NÃO É PRIMO!")
    n = int(input("Digite um número inteiro maior que 0: "))