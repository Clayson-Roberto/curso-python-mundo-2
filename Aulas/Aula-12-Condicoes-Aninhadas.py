''' Nessa aula, vamos aprender como criar estruturas condicionais
aninhadas, usando os comandos if.. elif.. else em programas Python. '''

nome = input('Digite seu nome: ')

if nome == 'Clayson':
    print(f'Que nome bonito você tem')
elif nome == "Pedro" or nome == 'Maria' or nome == 'Paulo':
    print(f'Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal')

print(f'Prazer em te conhecer {nome}')