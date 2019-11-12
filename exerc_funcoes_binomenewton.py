#### fazer uma funcao binominal que vai chamar a funcao fatorial 3x para n!/(k!(n-k)!)

import exerc_funcoes_fatorial

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

nf = (exerc_funcoes_fatorial.fatorial(n))
kf = (exerc_funcoes_fatorial.fatorial(k))

nk = (n - k)

nkf = (exerc_funcoes_fatorial.fatorial(nk))

bin = nf / (kf * nkf)

print("O resultado da equação binominal é: ",bin)

#equacao professor

def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))