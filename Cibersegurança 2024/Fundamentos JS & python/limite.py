from sympy import Symbol, limit, oo

# Definir a variável
x = Symbol('x')

# Definir a função
func = (x**2 - 4)/(x - 2)

# Calcular o limite quando x se aproxima de 2
limite = limit(func, x, 2)

print(f"O limite de (x^2 - 4)/(x - 2) quando x se aproxima de 2 é: {limite}")