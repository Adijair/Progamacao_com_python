matéria1 = int(input("Primeira nota: "))
matéria2 = int(input("segunda nota: "))
matéria3 = int(input("Teceira nota: "))

média = (matéria1 + matéria2 + matéria3) / 3

if média >= 7:
    print("O aluno foi aprovado, sua média foi:", média)
else:
    print("O aluno não foi aprovado, sua média foi:", média)
