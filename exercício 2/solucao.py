nota1 = float(input("Coloque sua nota "))
nota2 = float(input("Coloque sua nota "))
nota3 = float(input("Coloque sua nota "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5)/10

if media >= 6:
    print("Você foi aprovado, pois sua média foi de: ", media)

else:
    print("Você foi reprovado, pois sua nota foi: ", media)