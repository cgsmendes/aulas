dia=input("\n\nDigite o dia do aniversário da Isabela: ")
hora=input("\n\nDigite o horário do aniversário da Isabela: ")

import datetime
t=datetime.time(int(dia), int(hora))
print("\n\nVocê disse que o dia do aniversário é",dia,"às",hora,"horas.")

from datetime import datetime
now=datetime.now()

while int(dia)<int(now.day):
    dia=input("Dia anterior a hoje! Digite outra data: ")

dc=((int(dia)-int(now.day))*1440)
hc=((int(hora)-int(now.hour))*60)
mc=(int(dc)+int(hc))
dias=(mc//1440)
dr=(mc%1440)
horas=(dr+hc)//60
print("\n\nConsiderando que agora são",now.hour,":",now.minute,"do dia",now.day,", então o niver da Isabela começará em aproximadamente",dias,"dias e",horas,"horas")
print("\n\nOu seja, este é o tempo que você deverá esperar para beber todo o chopp do Diego!!!\n\n")
