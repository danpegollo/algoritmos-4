**Jogo de turno único:**

1\. O Novo Mecanismo de Jogo

Dados Oscilantes: O "Oráculo" gera valores que variam entre -10 e 10.
A Escolha Cega: Antes de revelar os dados, o jogador deve escolher um Fator de Multiplicação (FM) entre 1 e 3.
Cálculo de Impacto: O dano final é o valor absoluto da diferença entre os dados, multiplicado pelo fator escolhido.
Fórmula: Dano = |Dado\_Jogador - Dado\_Maquina| \* Fator multiplicador

2\. Requisitos Funcionais

Sorteio Oculto: O sistema sorteia os valores internamente (não exiba ainda!).
Dica técnica: Para gerar de -10 a 10: 
import random
print (random.randint(-10, 10))
Entrada do Usuário: Solicitar o Fator de Multiplicação (1, 2 ou 3).
Processamento:
Calcular a diferença absoluta.
Aplicar o multiplicador.

3\. Revelação e Condicionais:

Se Dado\_Jogador > Dado\_Maquina: Jogador vence e causa o dano calculado.
Se Dado\_Maquina > Dado\_Jogador: Máquina vence e o jogador recebe o dano.
Se iguais: Empate (dano zero).

Nesta versão avançada, o jogador deve tomar uma decisão estratégica antes de conhecer o resultado do sorteio. 
O objetivo é praticar a precedência de operadores, o uso de multiplicadores em variáveis e a lógica de tomada de decisão sob incerteza.

