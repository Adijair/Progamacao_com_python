produto = float(input("Digite o valor do produto: R$"))
desconto = float(input("Digite o pesentual de desconto: "))

valo_a_pagar = produto - (produto * desconto/100)

print("Preço do produto com desconto: {:.2f}".format(valo_a_pagar))