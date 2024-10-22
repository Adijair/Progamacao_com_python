# execute esses dois progamas


#carro nove ou velho, depende da idade usando o else
idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")


#rada de velocidade
velocidade = float(input("Digite a velocidade do seu carro km/h: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado em R$ {multa}")

if velocidade <= 80:
    print("Você não foi multado")
