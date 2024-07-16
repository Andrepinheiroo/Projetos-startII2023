# Vamos criar uma calculadora utilizando funções
def calculadora(n1, n2):
    '''
    Calculadora com as 4 operações!
    Para efetuar o cálculo, basta digitar um número por vez
    e posteriormente a operação que deseja realizar.

    O resultado será entregue em seguida!
    '''
    match op:
      case "+":
          print(f"{n1} + {n2} = {n1+n2}")
      case "-":
          print(f"{n1} - {n2} = {n1-n2}")
      case "*":
          print(f"{n1} * {n2} = {n1*n2}")
      case "/":
          if (n2 == 0):
              print("Impossível dividir por Zero!")
          else:             
              print(f"{n1} / {n2} = {(n1/n2)}")
      case default:
          print("Operação Inexistente!")


print(help(calculadora))
print()
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
op = input("Qual operação a ser realizada (+ - * /)? ")
print()

print(calculadora(n1, n2))


