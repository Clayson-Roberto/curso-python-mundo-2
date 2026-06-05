""" Crie um programa que leia uma frase qualquer e diga se ela é
um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA. """

userIsPhrase: str = str(input('Digite uma frase: ')).upper().strip() # Frase digitada pelo usuário
convertedUserPhrase = userIsPhrase.split() # A frase convertida para uma lista
sentence = ''.join(convertedUserPhrase) # A frase transformada em uma única string
invertedSentence = sentence[::-1] # Maneira de inverter sem usar o for para usar um '' no lugar de 'sentence[::-1]'

# Inverte a frase já transformada em string utilizando o laço for
'''for count in range(len(sentence) - 1, -1, -1):
    invertedSentence += sentence[count]'''

print(f'O inverso de {sentence} é {invertedSentence}')

# Verifica se é ou não um palíndromo
if sentence == invertedSentence:
    print('A frase digitada É um palíndromo.')
else:
    print('A frase digitada NÃO É um palíndromo.')