cigarros_dia = float(input("Quantos cigarros voce consome por dia: "))
anos_fumando = float(input("A quantos anos voce fuma: "))

total_cigarros = cigarros_dia * (anos_fumando * 365)  # Total de cigarros fumados
tempo_perdido_minutos = total_cigarros * 10  # Tempo perdido em minutos
tempo_perdido_anos = tempo_perdido_minutos / (24 * 60)  # Convertendo para anos

print(f"Você perdeu aproximadamente {tempo_perdido_anos:.2f} anos de vida devido ao hábito de fumar.")
