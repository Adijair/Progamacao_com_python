"""
x = 1
while x <= 3:
    print(x)
    x = x + 1 

# repetições com while
"""
"""
fim = int(input("Digite o utimo numoro a inprimir: "))
x = 1
while x <= fim:
    print(x)
    x = x + 1
    """

fim = int(input("Digite o utimo numoro a inprimir: "))
x = 1
while x <= fim:
    if x % 2 == 0:
        print(x)
        x = x + 1