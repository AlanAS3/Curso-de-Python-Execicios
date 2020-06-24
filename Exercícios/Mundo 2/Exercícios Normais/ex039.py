from datetime import date
print('==== Alistamento Militar ====')
Anas = int(input('Informe a seu ano de nascimento: '))
Aatual = int(date.today().year)
idade = Aatual - Anas
if idade == 18:
    print('É hora de fazer o Alistamento Militar!')
elif idade > 18:
    print('Já passou da hora de se Alistar!!')
    print(f'Já se passou {(idade) - 18} ano(s) do prazo')
else:
    print('Você ainda vai se Alistar')
    print(f'Ainda falta {18 - (idade)} ano(s) para o alistamento')
