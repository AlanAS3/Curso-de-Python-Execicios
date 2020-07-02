print('===== Índice de massa corporal ====')
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 < imc <= 25:
    print('Você está no seu PESO IDEAL')
elif 25 < imc <= 30:
    print('Você está no SOBREPESO')
elif 30 < imc <= 40:
    print('Você está na OBESIDADE')
else:
    print('Você está na OBESIDADE MÓRBIDA')
print(f'O seu IMC é: {imc:.1f}')
