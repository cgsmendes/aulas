import sys

n = int(input("Digite um número inteiro maior que 1: "))
x = n - 1

if n >= 1 and n <= 3:
    print(n, "É PRIMO!")
    sys.exit()
while x < n and x > 1:
    if n % x == 0:
        print(n,"NÃO NÃO NÃO!")
        sys.exit()
    else:
        x = x - 1
print(n, "É PRIMO!")