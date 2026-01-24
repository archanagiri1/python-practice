pesos = float(input("What do you have left in pesos?"))

soles = float(input("What do you have left in soles?"))

reais = float(input("What do you have left in reais?"))

pesos_to_usd = 0.0025
soles_to_usd = 0.27
reais_to_usd = 0.20

total_usd = (pesos*pesos_to_usd)+(soles*soles_to_usd)+(reais*reais_to_usd)

print(total_usd)