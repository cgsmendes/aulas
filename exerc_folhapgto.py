salario = float(input("Digite o seu salário: "))

if salario <= 280:
    reajuste = salario * 0.2
    print("Seu salário era de: ", salario, ", foi reajustado em 20%, sendo o reajuste no valor de: ", reajuste, ", e seu salário ficará em: ", salario + reajuste)
elif 280 < salario <= 700:
    reajuste = salario * 0.15
    print("Seu salário era de: ", salario, ", foi reajustado em 15%, sendo o reajuste no valor de: ", reajuste, ", e seu salário ficará em: ", salario + reajuste)
elif 700 < salario <= 1500:
    reajuste = salario * 0.1
    print("Seu salário era de: ", salario, ", foi reajustado em 10%, sendo o reajuste no valor de: ", reajuste, ", e seu salário ficará em: ", salario + reajuste)
else:
    reajuste = salario * 0.05
    print("Seu salário era de: ", salario, ", foi reajustado em 5%, sendo o reajuste no valor de: ", reajuste, ", e seu salário ficará em: ", salario + reajuste)