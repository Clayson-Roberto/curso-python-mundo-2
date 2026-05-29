''' Exercício Python 040: Crie um programa que leia duas
notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO '''

firstNote = float(input('Digite a primeira nota do aluno: ')) # Pede a primeira nota
secondNote = float(input('Digite a segunda nota do aluno: ')) # pede a segunda nota

average = (firstNote + secondNote) / 2 # Calcula a média do aluno

if average < 5: # Se a média for menor que 5
    print(f'Para uma média de {average:.2} o aluno está REPROVADO!')
elif average < 7: # Se a média menor que 7
    print(f'Para uma média de {average:.2} o aluno está de RECUPERAÇÃO!')
else: # Se a média for maior que 6.9
    print(f'Para uma média de {average:.2} o aluno está APROVADO!')
