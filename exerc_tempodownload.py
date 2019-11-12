tamanho = float(input("Digite o tamanho do arquivo em MB: "))
print("tamanho =", tamanho)
velocidade = float(input("Digite a velocidade da sua internet em Mbps: "))
print("tamanho =", velocidade)

tempo = ((tamanho * 8) / velocidade) / 60
print("O tempo aproximado de download deste arquivo é de:", tempo)