""" Desenvolva um programa que leia o primeiro termo e
a razão de uma PA. No final, mostre os 10 primeiros termos """

print(f'{'-=' * 30}')
print('10 Termos de uma PA')
print(f'{'-=' * 30}')

firstTerm = int(input('Primeiro termo: '))
reason = int(input('Qual a razão: '))

# Formula para saber o 10 termo se fosse o termo 20 mudaria o '(20 - 1)' assim para todo termo desejado
tenth = firstTerm + (10 - 1) * reason

for count in range(firstTerm, tenth, reason):
    print(f'{count}', end=' -> ')
print('Fim')
