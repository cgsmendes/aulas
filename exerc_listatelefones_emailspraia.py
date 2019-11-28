import os, glob, codecs
os.chdir('/Users/gustavomendes/PycharmProjects/aulas/emails')

for arquivo in glob.glob('*.txt'):
    arquivo = open('1.txt')
    for linha in arquivo:
        palavra = str("telefone:")
        if palavra in linha:
            tel = open('tel.txt', 'w')
            print(linha, "\n", file=tel)
            tel.close()
    #arquivo.close()
'''
import os
import codecs

DIRETORIO = '/Users/gustavomendes/PycharmProjects/aulas/emails/'

files = [f for f in os.listdir(DIRETORIO)]

lista_telefones = []

for f in files:
    linhas = codecs.open(DIRETORIO+"/"+f, 'r', "utf-8").readlines()
    for linha in linhas:
        if "telefone" in linha.lower():
            numero = linha.split(":")[1].rtrip().lstrip()
            lista_telefones.append(numero)

with open("tels.txt", "w") as out:
    for numero in lista_telefones:
        out.write(numero)
        out.write("\n")
'''