#MINHA FORMULA

import math

a=float(input("\nDigite o valor de A:\n\n"))
b=float(input("\nDigite o valor de B:\n\n"))
c=float(input("\nDigite o valor de C:\n\n"))

while a==0:
    a=float(input("O valor de 'a' não pode ser ZERO, por favor digite outro valor:\n\n"))

else:
    delta=b**2-4*a*c
    print("\n\nDelta é:",delta,"\n\n")

    if delta<0:
        print("Não tem raiz real.\n\n")

    elif delta==0:
        raiz1=(-b+math.sqrt(delta))/(2*a)
        print("Tem 1 raiz real.\n\n")
        print("A raiz real é:",raiz1,"\n\n")

    elif delta>0:
        raiz1=(-b+math.sqrt(delta))/(2*a)
        raiz2=(-b-math.sqrt(delta))/(2*a)
        print("Tem 2 raizes reais.\n\n")
        print("As raizes reais são:",raiz1,"\n\n")
        print("As raizes reais são:",raiz2,"\n\n")

#FORMULA PROFESSOR

deltaprof = b ** 2 - 4 * a * c

if deltaprof == 0:
    raiz1 =(-b + math.sqrt(deltaprof)) / (2 * a)
    print("EQUACAO PROF: A única raiz é: ", raiz1,"\n\n")
else:
    if deltaprof < 0:
        print("EQUACAO PROF: A equação não possui raízes reais\n\n")
    else:
        raiz1 = (-b + math.sqrt(deltaprof)) / (2 * a)
        raiz2 = (-b - math.sqrt(deltaprof)) / (2 * a)
        print("EQUACAO PROF: A primeira raiz é: ",raiz1,"\n\n")
        print("EQUACAO PROF: A segunda raiz é: ",raiz2,"\n\n")

