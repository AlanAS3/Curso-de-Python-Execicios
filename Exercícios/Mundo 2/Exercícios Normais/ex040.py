print('==== Média de aluno ====')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
med = (n1 + n2) / 2
if med < 5:
    print('O aluno foi REPROVADO!')
elif med >= 5 and med < 7:
    print('O aluno está em RECUPERAÇÂO!')
else:
    print('O aluno foi APROVADO!')
print(f'A média do aluno foi de: {med}')
