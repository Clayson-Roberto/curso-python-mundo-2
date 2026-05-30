""" Crie um programa que faça o computador jogar Jokenpô com você. """

from random import choice
from time import sleep

print('''Escolha uma das opções
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura''')

options = ['Pedra', 'Papel', 'Tesoura'] # Opções para o computador escolher
player = int(input('Qual a sua jogada? ')) # Opção escolhida pelo jogador
optionComputer = choice(options) # Opção escolhida pelo computador

# Verifica se o jogador colocou uma opção valida
if player > 3 or player < 1:
    print('Jogada invalida tente novamente!')
else:
    optionPlayer = options[player - 1] # Busca na lista 'options' a opção escolhida pelo jogador

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')

    print(f'{'-=' * 25}')
    print(f'Computador jogou {optionComputer}')
    print(f'Você jogou {optionPlayer}')
    print(f'{'-=' * 25}')

    # Se for empate
    if optionPlayer == optionComputer:
        print('Deu Empate!')

        # Vezes em que o computador ganha
    elif optionComputer == 'Pedra' and optionPlayer == 'Tesoura':
        print('O computador ganhou!')
    elif optionComputer == 'Tesoura' and optionPlayer == 'Papel':
        print('O computador ganhou!')
    elif optionComputer == 'Papel' and optionPlayer == 'Pedra':
        print('O computador ganhou!')

        # Vezes que o jagador ganha
    elif optionPlayer == 'Pedra' and optionComputer == 'Tesoura':
        print('Você ganhou!')
    elif optionPlayer == 'Tesoura' and optionComputer == 'Papel':
        print('Você ganhou!')
    elif optionPlayer == 'Papel' and optionComputer == 'Pedra':
        print('Você ganhou!')
