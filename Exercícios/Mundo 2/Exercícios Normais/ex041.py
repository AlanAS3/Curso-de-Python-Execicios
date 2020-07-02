from datetime import date
print('==== Classificando atletas ====')
nas = int(input('Em que ano você nasceu? '))
idade = int(date.today().year) - nas
if idade <= 9:
    print('Você está classificado como: MIRIM')
elif idade > 9 and idade < 15:
    print('Você está calssificado como: INFANTIL')
elif idade >= 15 and idade < 20:
    print('Você está classificado como: JUNIOR')
elif idade == 20:
    print('Você está classificado como: SÊNIOR')
else:
    print('Você está classificado como: MASTER')
