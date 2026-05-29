""" Refaça o DESAFIO 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes """

firstSegment = float(input('Digite o primeiro segmento: ')) # Primeiro segmento
secondSegment = float(input('Digite o segundo segmento: ')) # Segundo segmento
thirdSegment = float(input('Digite o terceiro segmento: ')) # Terceiro segmento

# Condição de existência: cada lado deve ser menor que a soma dos outros dois.
itIsTriangle = firstSegment < secondSegment + thirdSegment and secondSegment < firstSegment + thirdSegment and thirdSegment < secondSegment + firstSegment

if itIsTriangle: # Se os segmentos formarem um triângulo
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if firstSegment == secondSegment == thirdSegment: # Verifica se todos os segmentos são iguais
        print('EQUILÁTERO!')
    elif firstSegment != secondSegment != thirdSegment != firstSegment: # Verifica se todos os lados são diferentes
        print('ESCALENO!')
    else: # Se não pelo menos dois lados são iguais
        print('ISÓSCELES')
else: # Se os segmentos não formarem um triângulo
    print('Os segmentos a cima NÃO PODEM FORMAR um triângulo')
