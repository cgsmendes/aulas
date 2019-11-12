numero=int(input("Digite seu número: "))
y=0
z=1

while numero != 0 and y != z:
    x=int(numero//10)
    y=int(numero%10)
    z=int(x%10)
    numero=x

if y==z:
    numero1 = print ("O número tem adjacentes iguais!")
else:
    print("O número não tem adjacentes iguais!")