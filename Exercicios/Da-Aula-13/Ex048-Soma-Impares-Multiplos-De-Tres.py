""" Faça um programa que calcule a soma entre todos os números que são ímpares e
são múltiplos de três e que se encontram no intervalo de 1 até 500. """
calculate = 0
times = 0

for count in range(1, 501, 2):
    if count % 3 == 0:
        times += 1
        calculate += count

print(f'O valor calculado foi {calculate}, a quantidade de número calcula foi {times}')