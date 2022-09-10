# Jogo Pedra-Papel-Tesoura_Lagarto_Spok
# Autores: Luiz Carlos Martin Junior
#          Tamy Gabrielle da S. Martins
#
# As regras sao explicadas por Sheldon em The Big Bang Theory
# Vida longa a Sam Kass

import random

nomePlayer1 = input("Digite o seu nome: ")
nomePlayer2 = 'Computador'

elementos = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura', 4: 'Lagarto', 5: 'Spock'}
print('\033[0;97m*' * 20)
for i in range(5):
    print(f'{i + 1} - {elementos[i + 1]}')
print('x - para sair')
print('*' * 20)
print()

while True:
    escolha = input('Digite a opção desejada: ')
    if (escolha.upper() == 'X'):
        print("Obrigado por jogar!")
        break
    try:
        player1 = int(escolha)
    except:
        print('\033[1;30;41m    Digite uma opção válida    \033[0;97m')
        continue
    if (not 1 <= player1 <= 5):
        print('\033[1;30;41m    Digite uma opção válida    \033[0;97m')
        continue
    player2 = random.randint(1, 5)

    print()
    print(f"Opção de {nomePlayer1.title()}: {elementos[player1]}")
    print(f"Opção do {nomePlayer2}: {elementos[player2]}")

    print()
    player1_ganha = {1: {3, 4}, 2: {1, 5}, 3: {2, 4}, 4: {2, 5}, 5: {1, 3}}
    verbo1_ganha2 = {1: {3: ' quebra a ', 4: ' esmaga o '}, 2: {1: ' cobre a ', 5: ' refuta o '},
                     3: {2: ' corta o ', 4: ' mata o '}, 4: {2: ' come o ', 5: ' envenena o '},
                     5: {1: ' vaporiza a ', 3: ' mata o '}}
    if (player1 == player2):
        print('\033[1;30;42m    EMPATE!!!    \033[0;97m')
    elif player2 in player1_ganha[player1]:
        print(
            f'\033[1;30;44m    {nomePlayer1.title()} ganhou!!!  {elementos[player1]}{verbo1_ganha2[player1][player2]}{elementos[player2]}     \033[0;97m')
    else:
        print(
            f'\033[1;30;45m    {nomePlayer2} ganhou!!!  {elementos[player2]}{verbo1_ganha2[player2][player1]}{elementos[player1]}    \033[0;97m')