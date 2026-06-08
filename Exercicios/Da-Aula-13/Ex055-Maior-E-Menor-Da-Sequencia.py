""" Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos. """

minor = 0
bigger = 0

for count in range(1, 6):
    weight = float(input(f'Digite o peso da {count}° pessoa: '.format(count)))

    if count == 1:
        minor = weight
        bigger = weight
    else:
        if weight > bigger:
            bigger = weight

        if weight < minor:
            minor = weight

print(f'O maior peso indicado foi o {bigger}kg')
print(f'O menor peso indicado foi o {minor}kg')