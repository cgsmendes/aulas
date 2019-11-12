import math

a = float(input("\nDigite o valor de A:\n\n"))
b = float(input("\nDigite o valor de B:\n\n"))
c = float(input("\nDigite o valor de C:\n\n"))

def delta(a,b,c):
    return float((b**2)-(4*a*c))

def raiz1(a,b,c):
    return float((-b+math.sqrt((b**2)-(4*a*c)))/(2*a))

def raiz2(a,b):
    return float((-b-math.sqrt((b**2)-(4*a*c)))/(2*a))


while a==0:
    a=float(input("O valor de 'a' não pode ser ZERO, por favor digite outro valor:\n\n"))

else:
    print("\n\nDelta é:",delta(a,b,c),"\n\n")

    if delta(a,b,c)<0:
        print("Não tem raiz real.\n\n")

    elif delta(a,b,c)==0:
        print("Tem 1 raiz real.\n\n")
        print("A raiz real é:",raiz1(a,b,c),"\n\n")

    elif delta(a,b,c)>0:
        print("Tem 2 raizes reais.\n\n")
        print("As raizes reais são:",raiz1,"\n\n")
        print("As raizes reais são:",raiz2,"\n\n")