valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite quantos anos para paga: "))
meses = anos * 12
prestacao = valor / meses
if prestacao > salario * 0.3:
    print("Infeslimente você não vai pode receber o enprestimo. ")
else:
    print(f"O valor da prestação R${prestacao:7.2f}, enprestimo aprovado")


    #progama para aprovação de emprestimo..