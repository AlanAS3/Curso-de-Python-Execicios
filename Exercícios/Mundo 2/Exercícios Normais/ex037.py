print('==== Conversor de bases númericas ====')
n = int(input('Digite um número inteiro: '))
print("""[1] para Binário 
[2] para Octal
[3] para Hexadecimal""")
BasC = int(input('Digite a base para qual você deseja converter: '))
if BasC == 1:
    print(f'O número {n} convertido para Binário fica {bin(n)[2:].zfill(8)}')
elif BasC == 2:
    print(f'O número {n} convertido para Octal fica {oct(n)[2:]}')
elif BasC == 3:
    print(f'O número {n} convertido para Hexadecimal fica {hex(n)[2:]}')
