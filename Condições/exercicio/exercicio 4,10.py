consumo = int(input("Consumo de KWh: "))
tipo = input("Tipo da instalação(R ,I ou C): ")
if tipo == "R" or "r":
    if consumo <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo == "I" or "i":
    if consumo <= 1000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "C" or "c":
    if consumo <= 5000:
        preço = 0.55
    else:
        preço = 0.60
else:
    print("Erro tipo de instalação desconhecida.")
    preço = 0
custo = consumo * preço
print(f"Valor a paga R${custo:7.2f}")


# Calcula o preço do KWh consumido