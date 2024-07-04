salario_atual = float(input('Digite o salário atual do colaborador: R$ '))

if salario_atual <= 280:
    percentual= 20
elif salario_atual <= 700:
    percentual = 15
elif salario_atual <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + aumento

print(f'Salário antes do reajuste: R$ {salario_atual}')
print(f'Percentual de aumento aplicado: {percentual} %')
print(f'Valor do aumento: R$ {aumento}')
print(f'O novo salário, após o aumento é: R$ {novo_salario:}')