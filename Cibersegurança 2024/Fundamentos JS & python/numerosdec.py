n1 = int(input('Digite o número 1:'))
n2 = int(input('Digite o número 2:'))
n3 = int(input('Digite o número 3:'))

if n1 == n2 == n3:
    print('Todos os números são iguais.')
else:
    numeros = [n1, n2, n3]
    numeros.sort(reverse=True)

    print('Números em ordem decrescente é: ', numeros)