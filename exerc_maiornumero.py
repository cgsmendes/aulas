x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if z < x > y:
    print("O maior número é: ", x)
elif z < y > x:
    print("O maior número é: ", y)
else:
    print("O maior número é: ", z)