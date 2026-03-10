salario = float(input("Coloque seu salário: "))
tempo = int(input("Coloque seu tempo de trabalho em anos: "))

if tempo >= 5:
    bonus = 20
    salario = salario * 1.20
else:
    bonus = 10
    salario = salario * 1.10
print("O seu é bônus é de:", bonus, "% e seu salário com o bônus é:", salario)