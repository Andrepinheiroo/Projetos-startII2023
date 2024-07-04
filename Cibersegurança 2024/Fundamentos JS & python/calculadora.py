n1 = int(input('Digite o número 1:'))
n2 = int(input('Digite o número 2:'))
op =str(input('Digite a operação ( + - / * ):'))

if op == '+':
    resultado = n1 + n2
elif op == '-':
    resultado = n1 - n2
elif op == '*':
     resultado = n1 * n2
elif op == '/':
     if n2 == 0:
        resultado='não é possivel dividir por 0'
     else:resultado = n1 / n2
else: resultado= 'Operação inválida'

print(f'{n1} {op} {n2} = {resultado}')