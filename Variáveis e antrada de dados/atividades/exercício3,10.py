salário = float(input("Digite o valo do seu salário: R$"))
aumento = float(input("Digite o valo do almento:"))

novo_salário = salário + (salário * aumento / 100)

print("O salário com o almento sera: R${:.2f}".format(novo_salário))