#rada de velocidade
velocidade = float(input("Digite a velocidade do seu carro km/h: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado em R$ {multa}")

if velocidade <= 80:
    print("Você não foi multado")
