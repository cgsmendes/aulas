a=int(input("\n\nDigite o número ao qual deseja somar as unidades: \n\n"))
c=0

while a!=0:
    b=int(a%10)
    c=c+b
    a=int(a//10)

print("\nA soma das unidades do número digitado é: ",c,"\n\n")
