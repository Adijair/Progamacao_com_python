PrimeiroNumerio = int(input("Digite o primeiro numero: "))
SegundoNumero = int(input("Digite o segundo numero: "))
x = 1
y = 0
while x <= SegundoNumero:
    y = y + PrimeiroNumerio
    x = x + 1
print(f"{PrimeiroNumerio} x {SegundoNumero} = {y}")