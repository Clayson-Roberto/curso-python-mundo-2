""" Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores. """

from datetime import date

olderAge = 0
youngerAge = 0

for count in range(1, 8):
    birthdayYear = int(input(f'Digite o {count}° ano de nascimento: '))
    if date.today().year - birthdayYear < 18:
        youngerAge += 1
    else:
        olderAge += 1

print(f'''Ao todo são {olderAge} pessoas maiores de idade. 
E {youngerAge} pessoas menores de idade.''')