""" Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros """

print(f'{'-=' * 30}')
print('Bem vindo a loja dos seus sonhos')
print(f'{'-=' * 30}')

purchaseValue = float(input('Qual o valor do produto? R$')) # Valor total do produto

# Opções de pagamento
print('''Opção de pagamento
[ 1 ] - À vista dinheiro/cheque
[ 2 ] - À vista no cartão
[ 3 ] - Duas vezes no cartão
[ 4 ] - 3 ou mais vezes no cartão''')

option = int(input('Opção desejada:')) # Opção escolhida
finalValue = 0 # Valor final dependendo da opção escolhida

if option == 1:
    finalValue = purchaseValue - ((purchaseValue * 10) / 100)
elif option == 2:
    finalValue = purchaseValue - ((purchaseValue * 5) / 100)
elif option == 3:
    installments = purchaseValue / 2
    finalValue = purchaseValue
    print(f'A compra será parcelada em 2X de R$ {installments:.2f} sem juros')
elif option == 4:
    times = int(input('Quantas parcelas deseja pagar?'))
    finalValue = purchaseValue + ((purchaseValue * 20) / 100)
    installments = finalValue / times
    print(f'A compra será parcelada em {times}X de R$ {installments:.2f} com juros')
else:
    finalValue = purchaseValue
    print('Opção invalida por favor tente novamente!')

print(f'Sua compra de R$ {purchaseValue:.2f} vai custar R$ {finalValue:.2f} no final!')