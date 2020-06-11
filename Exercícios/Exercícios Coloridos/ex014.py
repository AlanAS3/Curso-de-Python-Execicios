print('\033[32;1m==== Conversor de Temperatura ====\033[m')
C = float(input('\033[31mInforme a temperatura em °C: '))
F = C * 1.8 + 32
print(f'\033[36mA conversão de {C:.1f}°C para Fahrenheit é \033[34;1m{F:.1f}°F')
