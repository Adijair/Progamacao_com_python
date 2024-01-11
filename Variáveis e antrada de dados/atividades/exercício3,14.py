dias_carro = float(input("Quantidade de dias que o carro foi alugado: "))
km_carro = float(input("Quantos km percorrido: "))

preço_total = (dias_carro * 60) + (km_carro * 0.15)

print("O valor a ser pago é R${:.2f}".format(preço_total))