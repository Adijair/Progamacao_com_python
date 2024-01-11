distancia = float(input("Digite a distancia da viagem em km: "))
velocidade_media = float(input("Dijite a velocidade media do carra: "))

tempo_da_viajem = distancia/velocidade_media

print("O tempo estimado sera aproximadamente {:.2f} horas.".format(tempo_da_viajem))