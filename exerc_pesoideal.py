sexo = int(input("Olá seu sexo é Masculino ou Feminino? Responda 0 para Masc. ou 1 para Fem.: "))
if sexo != 0 or sexo != 1:
    print("Digite somente 0 ou 1.")
    if sexo == 0:
        altura = float(input("Digite a sua altura: "))
        pesom = (72.7 * altura) - 58
        print("O peso médio ideal para homens é: ",pesom)
    elif sexo == 1:
        altura = float(input("Digite a sua altura: "))
        pesof = (62.1 * altura) - 44.7
        print("O peso médio ideal para mulheres é: ", pesof)
