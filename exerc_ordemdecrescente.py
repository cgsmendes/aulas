x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x > y and x > z and y > z:
    print(x, y, z)
elif x > y and x > z and z > y:
    print(x, z, y)
elif y > x and y > z and x > z:
    print(y, x, z)
elif y > x and y > z and z > x:
    print(y, z, x)
elif z > x and z > y and x > y:
    print(z, x, y)
else:
    print(z, y, x)