''' Escreva um programa que leia dois números inteiros
e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais '''

primeiroNumero = int(input('Digite o primeiro número inteiro: '))
segundoNumero = int(input('Digite o segundo número inteiro: '))

if primeiroNumero > segundoNumero:
    print(f'O primeiro número -> {primeiroNumero} é maior que o segundo número -> {segundoNumero}!')
elif segundoNumero > primeiroNumero:
    print(f'O segundo número -> {segundoNumero} é maior que o primeiro número -> {primeiroNumero}!')
else:
    print(f'Os números -> {primeiroNumero} e o -> {segundoNumero} são iguais!')
