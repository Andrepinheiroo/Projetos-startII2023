numeros = []

for i in range(1,6):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

soma = 0
for numero in numeros:
    soma += numero

print(f"A soma de todos os valores digitados é: {soma}")