cigarros_dia = float(input("Quantos cigarros voce consome por dia: "))
anos_fumando = float(input("A quantos anos voce fuma: "))

minutos = (anos_fumando * 365) * cigarros_dia * 10 

dias_perdidos = minutos / 1440

print(dias_perdidos)