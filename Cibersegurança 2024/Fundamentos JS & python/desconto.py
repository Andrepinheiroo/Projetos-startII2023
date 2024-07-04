vhora = int(input('Digite o valor da sua hora: R$ '))
horastrab= int(input('Digite a quantidade de horas trabalhadas no mês: '))

bruto = vhora * horastrab

if bruto <= 900:
    p_ir = 0
elif bruto <= 1500:
    p_ir = 5
elif bruto <= 2500:
    p_ir = 10
else:
    p_ir = 20

desconto_ir = bruto * (p_ir / 100)
desconto_inss = bruto * 0.10
fgts = bruto * 0.11
desconto_sindicato = bruto * 0.03


total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = bruto - total_descontos


print(f'Salário Bruto ({vhora:.2f} * {horastrab})  : R$ {bruto:.2f}')
print(f'(-) IR ({p_ir}%)                 : R$ {desconto_ir:.2f}')
print(f'(-) INSS (10%)               : R$ {desconto_inss:.2f}')
print(f'(-) Sindicato (3%)           : R$ {desconto_sindicato:.2f}')
print(f'FGTS (11%)                   : R$ {fgts:.2f}')
print(f'Total de descontos           : R$ {total_descontos:.2f}')
print(f'Salário Líquido              : R$ {salario_liquido:.2f}')