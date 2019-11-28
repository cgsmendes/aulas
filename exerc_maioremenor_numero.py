x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if z < x > y > z:
# OU if x > y and x > z and y > z:
    print("O maior número é: ", x)
    print("O menor número é: ", z)
elif x > y and x > z and z > y:
    print("O maior número é: ", x)
    print("O menor número é: ", y)
elif y > x and y > z and x > z:
    print("O maior número é: ", y)
    print("O menor número é: ", z)
elif y > x and y > z and z > x:
    print("O maior número é: ", y)
    print("O menor número é: ", x)
elif z > x and z > y and x > y:
    print("O maior número é: ", z)
    print("O menor número é: ", y)
else:
    print("O maior número é: ", z)
    print("O menor número é: ", x)