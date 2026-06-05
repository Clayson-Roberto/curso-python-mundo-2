""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

num = int(input('Digite um número: '))
timesDivisible = 0

for count in range(1, num + 1):
    if num % count == 0:
        print('\033[34m', end=' ')
        timesDivisible += 1
    else:
        print('\033[31m', end=' ')

    print(f'{count}', end=' ')

print(f'\n\33[38mO número {num} foi divido {timesDivisible} vezes.')

if timesDivisible == 2:
    print('E por isso ele È PRIMO')
else:
    print('E por isso ele NÂO É PRIMO')