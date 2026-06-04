""" Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o. """

sum = 0

for count in range(1, 7):
    number = int(input(f'Digite o {count}° número: '))
    if number % 2 == 0:
        sum += number

print(f'A soma de todos os números pares é {sum}')