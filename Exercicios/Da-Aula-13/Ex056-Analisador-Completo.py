""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. """

fullAge = 0 # Variavel para calcular idade total
nameOfTheOldest = '' # Variavel para guardar o nome do homem mais velho
howManyWomen = 0 # Variavel para saber quantas mulheres menores de 20 anos foram passadas
olderMan = 0 # Variavel para calcular o homem mais velhor

for count in range(1, 5):
    print(f'{'-=' * 15} Cadastro da {count}° pessoa {'-=' * 15}')
    name = input(f'Digite o nome da {count}° pessoa: ').strip()
    age = int(input(f'Digite a idade da {count}° pessoa: '))
    sex = input(f'Digite o sexo da {count}° [M / F]: ').upper().strip()

    fullAge += age # Soma as idades totais

    if sex == 'F':
        if age < 20:
            howManyWomen += 1

    if sex == 'M':
        if age > olderMan:
            olderMan = age
            nameOfTheOldest = name

print(f'O homem mais velho é {nameOfTheOldest.capitalize()}.')
print(f'A média de idade entre as pessoas informadas é {fullAge / 4} anos')
print(f'A quantidade de mulheres informada com menos de 20 anos é de {howManyWomen}')