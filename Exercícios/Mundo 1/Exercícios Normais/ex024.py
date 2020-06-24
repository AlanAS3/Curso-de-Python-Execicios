print('=== Analisando o nome da cidade ===')
cidade = str(input('Digite o nome da sua cidade: ')).strip()
cidade = cidade.upper().split()
print(f'A cidadde começa com a letra SANTOS: {"SANTO" in cidade[0]}')
