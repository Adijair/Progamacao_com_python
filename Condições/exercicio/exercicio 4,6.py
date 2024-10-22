distancia = float(input("Digite a distancia da sua viagem em KM: "))

if distancia <= 200:
    passagem = 0.50 * distancia
else:
    passagem = 0.45 * distancia

print(f"o valor da sua passagem vai ser de R${passagem}.")