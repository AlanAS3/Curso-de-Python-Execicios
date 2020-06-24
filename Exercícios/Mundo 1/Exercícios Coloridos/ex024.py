print('\033[32;1m=== Analisando o nome da cidade ===\033[m')
cidade = str(input('\033[31mDigite o nome da sua cidade: ')).strip()
cidade = cidade.upper().split()
print(f'\033[36mA cidadde começa com a letra SANTOS: \033[34;1m{"SANTO" in cidade[0]}')
