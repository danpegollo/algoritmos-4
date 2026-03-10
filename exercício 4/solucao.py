import random

dado_Jogador = random.randint(-10, 10)
dado_Maquina = random.randint(-10, 10)
fator = int(input("Escolha um fator de multiplicação de 1 a 3: "))

if fator > 4 or fator < 1:
    print("Coloque o valor correto para o fator multiplicador")
else:
    dano = (dado_Jogador - dado_Maquina) * fator
    if dado_Jogador > dado_Maquina:
        print("O dado saiu", dado_Jogador, "e da máquina", dado_Maquina, "jogador vence, e o jogador causa o dano", dano)
    elif dado_Jogador < dado_Maquina:
        print("O dado saiu", dado_Jogador, "e da máquina", dado_Maquina, "maquina vence, e o jogador leva o dano", dano)
    else:
        print("O dado saiu", dado_Jogador, "e da máquina", dado_Maquina, "deu empate e o dano sofrido é de zero") 