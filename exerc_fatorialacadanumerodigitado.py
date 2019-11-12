import exerc_funcoes_fatorial

numero = int(input("Digite um número inteiro positivo que deseja calcular o fatorial: "))
while numero >= 0:
    fatorial = exerc_funcoes_fatorial.fatorial(numero)
    print("O fatorial de", numero, "é:", fatorial)
    numero = float(input("Digite um número inteiro positivo que deseja calcular o fatorial: "))