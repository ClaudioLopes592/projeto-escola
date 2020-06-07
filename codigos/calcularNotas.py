nome = str(input('Digite o nome do aluno: ')).upper()
turma = str(input('Digite a turma: '))
periodo = str(input('Digite o período: ')).upper()
professor = str(input('Digite o nome do professor: ')).upper()
materia = str(input('Digite a matéria: ')).upper()
print('x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x')
print('Nome do aluno: {} '.format(nome))
print('Turma: {} '.format(turma))
print('Período: {} '.format(periodo))
print('Nome do professor: {} '.format(professor))
print('Matéria: {} '.format(materia))
print('x.x.x.x.x.x.x.x.x.x N O T A S x.x.x.x.x.x.x.x.x.x')
nota = 1
cont = 1
opcao = 'S'
while opcao == 'S':
    nota = float(input('Entre com a {}.ª nota deste aluno: '.format(cont)))
    cont += 1
    opcao = str(input('Deseja informar outra nota? [S|N]')).upper()
else:
    pass
print('x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x')