""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida """

kilos = float(input('Quantos Kg você pesa? (Kg):')) # Pega o quilo da pessoa
height = float(input('Qual é sua altura? (m):')) # Pega a altura da pessoa
imc = kilos / (height * height) # Calcula o IMC 'quilos / (altura * altura)'

print(f'O IMC desta pessoa é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está com sobrepeso!')
elif imc <= 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida')
