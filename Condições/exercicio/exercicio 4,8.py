a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação (+, -, * ou /):")
if operacao == "+":
    resutado = a + b
elif operacao == "-":
    resutado = a - b
elif operacao == "*":
    resutado = a * b
elif operacao == "/":
    resutado =  a / b
else:
    print("Operação invalida.")
    resutado = 0
print("O resutado foi", resutado) 