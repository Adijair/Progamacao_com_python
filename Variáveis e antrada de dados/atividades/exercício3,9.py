#programa que leia a quantidade de dias, horas, minutos e segundos do usuário. calcule o total em segundos 

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total_segundos = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print("O total em segundos é:", total_segundos)
