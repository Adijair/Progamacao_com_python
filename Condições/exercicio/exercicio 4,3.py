a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o tercero valor:"))

maior = a

if b > a and b > c: # se B é maior que A e B é maior que C ent o B vai ser o maior
    maior = b
if c > a and c > b: # se C é maior que A e C é maior que B ent o C vai ser o maior
    maior = c

menor = a

if b < c and b < a: # se B é menor que C e B é menor que C ent o B vai ser o menor
    maior = b
if c <= b and c < a: # se C é menor ou igual a B e C é menor que A ent o C vai ser o menor
    menor = c

print(f"O menor número foi {menor}")
print(f"O maior número foi {maior}")