""" Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for. """

number = int(input('Digite um número para saber sua tabuada:'))

for count in range(1, 11):
    print(f'{number} X {count:2} = {number*count}')