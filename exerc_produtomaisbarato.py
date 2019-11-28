x = float(input("Digite o primeiro produto: "))
y = float(input("Digite o segundo produto: "))
z = float(input("Digite o terceiro produto: "))

if z < x > y > z:
# OU if x > y and x > z and y > z:
    print("O produto mais barato é: ", z)
elif x > y and x > z and z > y:
    print("O produto mais barato é: ", y)
elif y > x and y > z and x > z:
    print("O produto mais barato é: ", z)
elif y > x and y > z and z > x:
    print("O produto mais barato é: ", x)
elif z > x and z > y and x > y:
    print("O produto mais barato é: ", y)
else:
    print("O produto mais barato é: ", x)