salario = float(input("Digite o seu salário: "))

f_aumento = 0.15 # aumento de 15%

if salario > 1250: # se o seu salario for maior que 1250 voce ira receber um aumento de 10%
    f_aumento = 0.10

aumento = salario * f_aumento
print(f"Seu aumento vai ser de: {aumento}")