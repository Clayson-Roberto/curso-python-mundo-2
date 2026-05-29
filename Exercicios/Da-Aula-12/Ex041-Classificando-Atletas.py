''' A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER '''

from datetime import date

currentYear = date.today().year # Pega o ano atual
yearOfBirth = int(input('Digite o ano de nascimento do atleta: ')) # Pega o ano de nascimento do atleta

age = currentYear - yearOfBirth # Calcula quantos anos o atleta tem

print(f'O atleta tem {age} anos')

if age <= 9: # Atletas com 9 anos ou menos
    print(f'Categoria: MIRIM')
elif age <= 14: # Atletas com 14 anos ou menos
    print(f'Categoria: INFANTIL')
elif age <= 19: # Atletas com 19 anos ou menos
    print(f'Categoria: JÚNIOR')
elif age <= 25: # Atletas com 25 anos ou menos
    print(f'Categoria: SÊNIOR')
else: # Atletas com mais de 25 anos
    print(f'Categoria: MASTER')