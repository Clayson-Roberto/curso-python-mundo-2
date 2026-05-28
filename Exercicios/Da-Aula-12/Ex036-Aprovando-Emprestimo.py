''' Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado. '''

valorDaCasa = float(input('Digite o valor da casa: '))
salario = float(input('Qual seu salário: '))
anosParaPagar = int(input('Quantos anos você vai pagar: '))

valorMensalDaCasa = valorDaCasa / (anosParaPagar * 12)

print(f'Para pagar uma casa de R$ {valorDaCasa:.2f} em {anosParaPagar} anos')
print(f'Aprestação será de R$ {valorMensalDaCasa:.2f}')

if valorMensalDaCasa >= salario * 30 / 100:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
