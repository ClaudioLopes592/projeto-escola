def titulo(txt):
    print('-' * 40)
    print(txt)
    print('-' * 40)

def linha():
    print('-' * 40)

nome = str(input('Digite o nome do aluno: ')).upper()
turma = str(input('Digite a turma: '))
periodo = str(input('Digite o período: ')).upper()
professor = str(input('Digite o nome do professor: ')).upper()
materia = str(input('Digite a matéria: ')).upper()
titulo('            SISTEMA ESCOLAR          ')
print(f'Nome do aluno: {nome}')
print(f'Turma: {turma}')
print(f'Período: {periodo}')
print(f'Nome do professor: {professor}')
print(f'Matéria: {materia}')
titulo('            N O T A S              ')
notas = []
soma = 0
cont = 1
opcao = 'S'
while opcao == 'S':
    nota = float(input(f'Entre com a {cont}.ª nota deste aluno: '))
    notas.append(nota)
    quant = len(notas)
    soma += nota
    media = soma / quant
    cont += 1
    opcao = str(input('Deseja informar outra nota? [S|N]')).upper()
else:
    pass

if media >= 7:
    print('A média das notas apuradas do aluno {} é {:.1f} - APROVADO'.format(nome,media))
elif media >= 5 and media < 7:
    print('A média das notas apuradas do aluno {} é {:.1f} - RECUPERAÇÃO'.format(nome,media))
else:
    print('A média das notas apuradas do aluno {} é {:.1f} - REPROVADO'.format(nome,media))    

linha()