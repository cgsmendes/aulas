valorhora = float(input("Digite quanto ganha por hora: "))
hora = float(input("Digite o número de horas trabalhadas no mês: "))
salariobruto = valorhora * hora
ir = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
liquido = salariobruto - ir - inss - sindicato
print("Seu salário bruto é de: ",salariobruto)
print("Você pagou R$ ",ir," de IR.")
print("Você pagou R$ ",inss," ao INSS.")
print("Você pagou R$ ",sindicato," ao Sindicato.")
print("Seu salário líquido é de R$ ",liquido)