""" Nessa aula, vamos começar nossos estudos com os laços e vamos
fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):
    print(c)
print(‘Acabou’) """


""" Iniciando com repetição """
# O 'count' é usado como referência podendo ser qualquer nome,
# O 'range(1, 6)' para referenciar quantas vezes deve se repetir a estrutura que esta dentro do laço
print('Contagem de 1 até 5')
for count in range(1, 6):
    print(count)
print('Fim')
print(f'{'-=' * 30}')

# Para que a contagem seja diminuindo precisa colocar o -1 ao final para
# que o laço entenda que deve retirar e não colocar
print('Contagem de 6 até 1')
for count in range(6, 0, -1):
    print(count)
print('Fim')
print(f'{'-=' * 30}')

# A última interação indica em que ponto deve ser executado a iteração
print('Contagem de 1 até 6 pulando de dois em dois ')
for count in range(0, 7, 2):
    print(count)
print('Fim')
print(f'{'-=' * 30}')

# Pode também usar uma variável para ser utilizada como referência para os laços
# O '+ 1' seria para que o contador fosse até o número desejado
# pelo motivo dele ignorar o último número
print('Utilizando uma variável para ser referenciada no laço de repetição')
numerTeste1 = int(input('Digite um número inteiro: '))
for count in range(0, numerTeste1 + 1):
    print(count)
print('Fim')
print(f'{'-=' * 30}')

# Podendo substituir qualquer valor referenciado no laço
print('Interagindo com todos os valores do laço através de uma variável')
start = int(input('Digite o número de inicio: '))
end = int(input('Digite o número do fim: '))
steps = int(input('Digite de quantas e quantas vezes ele deve pular: '))

for count in range(start, end + 1, steps):
    print(count)
print('Fim')
print(f'{'-=' * 30}')

# Usando o laço para somar uma quantidade de número passado por interação com o usuário
print('Somando números através de uma interação')
sumTeste1 = 0
for count in range(0, 4):
    num = int(input('Digite valor para ser somado: '))
    sumTeste1 += num # O 'sumTeste1 += num' é usado para substituir 'sumTeste1 = sumTeste1 + num'
print(f'A soma dos valores digitados é {sumTeste1}')