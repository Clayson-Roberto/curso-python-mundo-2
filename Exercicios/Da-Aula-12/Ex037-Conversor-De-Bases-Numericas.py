''' Escreva um programa em Python que leia um número
inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário,
2 para octal e
3 para hexadecimal. '''

numero = int(input('Digíte um número inteiro: '))

print('[ 1 ] -> Para binário')
print('[ 2 ] -> Para octal')
print('[ 3 ] -> Para hexadecimal')

opcaoEscolhida = int(input('Qual conversão você deseja: '))

if opcaoEscolhida == 1:
    print(f'O número {numero} convertido para binário é -> {bin(numero)[2:]}')
elif opcaoEscolhida == 2:
    print(f'O número {numero} convertido para octal é -> {oct(numero)[2:]}')
elif opcaoEscolhida == 3:
    print(f'O número {numero} convertido para hexadecimal é -> {hex(numero)[2:]}')
else:
    print('Opção invalida tente novamente!')
