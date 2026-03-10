preco = int(input("Coloque o valor do produto: "))

nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = nota1 = 0

if preco >= 100:
    nota100 = preco // 100
    preco = preco % 100

if preco >= 50:
    nota50 = preco // 50
    preco = preco % 50

if preco >= 20:
    nota20 = preco // 20
    preco = preco % 20

if preco >= 10:
    nota10 = preco // 10
    preco = preco % 10

if preco >= 5:
    nota5 = preco // 5
    preco = preco % 5

if preco >= 2:
    nota2 = preco // 2
    preco = preco % 2

if preco >= 1:
    nota1 = preco

print("Notas necessárias:")
print("100:", nota100)
print("50:", nota50)
print("20:", nota20)
print("10:", nota10)
print("5:", nota5)
print("2:", nota2)
print("1:", nota1)