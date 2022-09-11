# Jogo Pedra-Papel-Tesoura_Lagarto_Spok
# Autores: Luiz Carlos Martin Junior
#          Tamy Gabrielle da S. Martins
#
# As regras sao explicadas por Sheldon em The Big Bang Theory
# Vida longa a Sam Kass

import random

nomePlayer1 = input("Digite o seu nome: ")
nomePlayer2 = 'Computador'

# o dicionario abaixo contem letra branca (30) com o fundo descrito
cor_fundo = {'normal': '\033[m',
             'vermelho': '\033[1;30;41m',
             'verde': '\033[1;30;42m',
             'azul': '\033[1;30;44m',
             'roxo': '\033[1;30;45m',
             'Azul claro': '\033[1;30;46m',
             'cinza': '\033[1;30;47m'}
elementos = {1: 'Pedra',
             2: 'Papel',
             3: 'Tesoura',
             4: 'Lagarto',
             5: 'Spock'}

print('\033[0;97m*' * 20)
for i in range(5):
    print(f'{i + 1} - {elementos[i + 1]}')
print('x - para sair')
print('*' * 20)
print()

while True:
    print()
    escolha = input('Digite a opção desejada: ')
    if (escolha.upper() == 'X'):
        print("Obrigado por jogar!")
        break
    try:
        player1 = int(escolha)
    except:
        print(f"{cor_fundo['vermelho']}    Digite uma opção válida    {cor_fundo['normal']}")
        continue
    if (not 1 <= player1 <= 5):
        print(f"{cor_fundo['vermelho']}    Digite uma opção válida    {cor_fundo['normal']}")
        continue
    player2 = random.randint(1, 5)

    print()
    print(f"Opção de {nomePlayer1.title()}: {elementos[player1]}")
    print(f"Opção do {nomePlayer2}: {elementos[player2]}")

    player1_ganha = {1: {3, 4}, 2: {1, 5}, 3: {2, 4}, 4: {2, 5}, 5: {1, 3}}
    verbo1_ganha2 = {1: {3: ' amassa a ', 4: ' esmaga o '},
                     2: {1: ' cobre a ', 5: ' refuta o '},
                     3: {2: ' decapita o ', 4: ' mata o '},
                     4: {2: ' come o ', 5: ' envenena o '},
                     5: {1: ' vaporiza a ', 3: ' quebra o '}}
    if (player1 == player2):
        print(f"{cor_fundo['verde']}    EMPATE!!!    {cor_fundo['normal']}")
    elif player2 in player1_ganha[player1]:
        print(f"{cor_fundo['azul']}    {nomePlayer1.title()} ganhou!!!  {elementos[player1]}{verbo1_ganha2[player1][player2]}{elementos[player2]}     {cor_fundo['normal']}")
    else:
        print(f"{cor_fundo['roxo']}    {nomePlayer2} ganhou!!!  {elementos[player2]}{verbo1_ganha2[player2][player1]}{elementos[player1]}    {cor_fundo['normal']}")