''' Faça um programa que leia o ano de nascimento de um
jovem e informe, de acordo com a sua idade, se ele ainda
vai se alistar ao serviço militar, se é a hora exata de
se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo. '''

# Desafio extra se for mulher deve informar que o alistamento não é obrigatório

from datetime import date

anoDeNasc = int(input('Digite seu ano de nascimento: ')) # Pega o ano de nascimento
sexo = str(input('Digite seu sexo (M/F): ')).upper().strip() # Pega o sexo da pessoa
anoAtual = date.today().year # Pega o ano atual
idade = anoAtual - anoDeNasc # Calcula quantos anos a pessoa tem
anoDoAlistamento = anoDeNasc + 18 # Calcula o ano de alistamento

if idade < 18:
    if 18 - idade == 1:
        print(f'Ainda falta {18 - idade} ano para o alistamento!')
    else:
        print(f'Ainda falta {18 - idade} anos para o alistamento!')
        print(f'Seu alistamento será em {anoDoAlistamento}')
elif idade == 18:
    print(f'Você deve se alistar esse ano, vá agora mesmo a uma Junta Militar!!!')
else:
    if idade - 18 == 1:
        print(f'O seu alistamento foi há {idade - 18} ano')
    else:
        print(f'O seu alistamento foi há {idade - 18} anos')
        print(f'Seu alistamento foi em {anoDoAlistamento}')

if sexo == 'F':
    print('O alistamento não é obrigatório para mulheres')