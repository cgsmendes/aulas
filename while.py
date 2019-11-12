i=0

while i<=10:
    print(2**i)
    i=i+1
    

#OUTRO EXERCICIO

print("Digite uma sequencia de valores finalizando com o ZERO.")

soma=0
valor=1

while valor!=0:
    valor=float(input("\nDigite um valor a ser somado: "))
    soma=soma+valor

print("\nA soma dos valores digitados é: ",soma,"\n\n")



#OUTRO EXERCICIO

tamanho=int(input("Digite o tamanho da sequencia de números: "))

produto=1
i=0

while i<tamanho:
    valor=int(input("\nDigite um valor a ser multiplicado: "))
    produto=produto*valor
    i=i+1

print("\nO produto dos valores digitados é: ",produto,"\n\n")
