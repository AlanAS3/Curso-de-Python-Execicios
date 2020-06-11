print('\033[32;1m==== Aumento de salário (15%) ====\033[m')
sal = float(input('\033[31mSalário atual do funcionario R$ '))
Nsal = float(sal + ((15/100)*sal))
print(f'\033[36mO novo salário do funcionário é de R$\033[34;1m{Nsal:.2f}')
